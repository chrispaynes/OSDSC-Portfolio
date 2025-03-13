import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from IPython.display import display
from sklearn.linear_model import ElasticNetCV
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from statsmodels.api import qqplot
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor


def create_heatmap(
    data,
    title="DataFrame Correlation Heatmap",
    figsize=(50, 40),
    fontsize=48,
    title_fontsize=75,
):
    plt.figure(figsize=figsize)

    mask = np.triu(np.ones_like(data.corr(), dtype=bool))

    heatmap = sns.heatmap(
        data.corr(),
        mask=mask,
        vmin=-1,
        vmax=1,
        annot=True,
        annot_kws={"fontsize": fontsize},
        fmt=".2f",
    )
    heatmap.set_xticklabels(heatmap.get_xmajorticklabels(), fontsize=fontsize)
    heatmap.set_yticklabels(heatmap.get_ymajorticklabels(), fontsize=fontsize)
    heatmap.set_title(title, fontdict={"fontsize": title_fontsize}, pad=2)
    plt.show()


def plot_error_lines(
    X_train,
    X_test,
    y_train,
    y_test,
    estimator,
    title="",
    x_label="CV Fold",
    xticks=[],
    scoring="neg_mean_absolute_error",
):
    x_points = np.arange(0, estimator.cv)

    train_accuracy = abs(
        cross_val_score(
            estimator, X_train, y_train, scoring=scoring, n_jobs=-1, cv=estimator.cv
        )
    )
    test_accuracy = abs(
        cross_val_score(
            estimator, X_test, y_test, scoring=scoring, n_jobs=-1, cv=estimator.cv
        )
    )

    summary_df = pd.DataFrame(
        {
            "# Variables": [X_train.shape[1]],
            f"Train {scoring} (absolute)": [np.round(np.mean(train_accuracy), 2)],
            f"Test {scoring} (absolute)": [np.round(np.mean(test_accuracy), 2)],
            "Best Model Params": [estimator.best_params_],
        }
    )

    try:
        important_feats = X_train.columns[
            estimator.estimator["feature_selection"].get_support()
        ]
        summary_df["Imp. Feats."] = [list(important_feats)]
        summary_df["# Imp. Feats."] = [len(important_feats)]
    except:
        # ignore errors when there's no 'feature_selection' step
        pass

    display(summary_df)

    plt.figure(figsize=(10, 5))
    plt.title(title)
    sns.regplot(
        x_points,
        y=train_accuracy,
        ci=None,
        line_kws={"linewidth": 1.5},
        label=f"Train {scoring} (absolute): {round(np.mean(train_accuracy), 4)}",
    )
    sns.regplot(
        x_points,
        y=test_accuracy,
        ci=None,
        line_kws={"linewidth": 1.5},
        label=f"Test {scoring} (absolute): {round(np.mean(test_accuracy), 4)}",
    )

    plt.legend()
    plt.xticks(xticks or range(estimator.cv))
    plt.xlabel(x_label)
    plt.ylabel(scoring)
    plt.show()


def plot_param_options_accuracy(
    X_train,
    X_test,
    y_train,
    y_test,
    pipeline,
    step,
    options,
    options_key,
    scoring="neg_mean_absolute_error",
    param_desc="",
    cv=5,
):
    # Setup arrays to store train and test scores
    opts_range = np.arange(1, len(options) + 1)
    train_scores = np.empty(len(opts_range))
    test_scores = np.empty(len(opts_range))

    for i, option in enumerate(options):
        # Fit the classifier to the training data
        pipeline.fit(X_train, y_train)
        estimator = GridSearchCV(pipeline, param_grid={f"{step}__{options_key}": [option]}, cv=cv).fit(
            X_train, y_train
        )

        # Compute score on the training set
        train_scores[i] = np.mean(
            abs(
                cross_val_score(
                    estimator, X_train, y_train, scoring=scoring, n_jobs=-1, cv=cv
                )
            )
        )

        # Compute score on the testing set
        test_scores[i] = np.mean(
            abs(
                cross_val_score(
                    estimator, X_test, y_test, scoring=scoring, n_jobs=-1, cv=cv
                )
            )
        )

        try:
            print(
                "feature_importances_",
                X_train.columns[pipeline["feature_selection"].get_support()],
            )
        except:
            # ignore errors when there's no 'feature_selection' step
            pass

    print(param_desc)
    plt.title(f"Varying {options_key}")
    plt.plot(options, train_scores, label="Test MAE")
    plt.plot(options, test_scores, label="Train MAE")
    plt.legend()
    plt.xlabel(f"{step} {options_key} options")
    plt.ylabel("Mean Absolute Error" or scoring)
    plt.show()


def plot_elastic_net_feature_importance(X_train, y_train):
    steps = [
        ("scaler", StandardScaler()),
        ("elasticNet", ElasticNetCV()),
    ]

    pipeline = Pipeline(steps).fit(X_train, y_train)

    reg = pipeline.named_steps.get("elasticNet")

    # The amount of penalization chosen by cross validation.
    coef = pd.Series(reg.coef_, index=X_train.columns)

    selected_vars = abs(coef) > 0
    selected_cols = coef[selected_vars == True].index
    print("ElasticNet selected", list(selected_cols))
    num_selected_vars = sum(selected_vars)

    print(
        f"ElasticNet selected {num_selected_vars} variables and eliminated { sum(abs(coef) == 0) } variables"
    )

    imp_coef = coef.sort_values()
    imp_coef = pd.DataFrame(
        {
            "Feature Importance": imp_coef,
            "Feature Importance (SN)": imp_coef.apply(np.format_float_scientific),
        }
    )
    imp_coef.reset_index(inplace=True)
    imp_coef = imp_coef.rename(columns={"index": "Feature"})

    barplot = sns.barplot(
        data=imp_coef, y="Feature", x="Feature Importance", orient="h"
    )
    barplot.set_title("ElasticNet Model Feature Importance")

    imp_coef[abs(imp_coef["Feature Importance"]) > 0]

    plt.show()

    return list(selected_cols)


def plot_feature_regression_results(model, x_cols):
    # This plots four graphs in a 2 by 2 figure: 'dependent versus independent variable',
    # 'residuals versus independent variable', 'fitted versus independent variable' and
    # 'fitted plus residual versus independent variable'
    for feature in x_cols:
        _ = sm.graphics.plot_regress_exog(
            model, feature, fig=plt.figure(figsize=(12, 8))
        )


def create_regression_model(df, x_cols, target_var):
    # creates OLS regression model using the dependent and independent variables

    f = f"{target_var} ~ {' + '.join(x_cols)}"

    return ols(
        formula=f,
        data=df,
    ).fit()


def print_OLS_results(model):
    rnd = lambda v: v.round(3)

    print("AIC", rnd(model.aic))
    print("R-Squared", rnd(model.rsquared))
    print("R-Squared Adjusted", rnd(model.rsquared_adj))
    print("Mean-Squared Error:", rnd(model.mse_resid))
    print("Residual Standard Error:", rnd(np.sqrt(model.mse_resid)), end="\n\n")
    print(model.summary())


def get_OLS_summary(X, y, output=True, qq_output=True):
    X = sm.add_constant(X)
    results = sm.OLS(y, X).fit()

    if qq_output:
        _ = qqplot(data=results.resid, fit=True, line="45")

    if output:
        print_OLS_results(results)

    return results


def filter_high_VIF_features(X, VIF_threshold=5):
    VIFS = {
        col: variance_inflation_factor(X.values, i).round(3)
        for i, col in enumerate(X)
    }

    VIF_df = pd.DataFrame({"Feature": VIFS.keys(), "VIF": VIFS.values()}).sort_values(
        by="VIF", ascending=False
    )

    VIF_df.style.hide_index()

    low_collinearity_df = VIF_df[VIF_df.VIF < VIF_threshold]

    return VIF_df, low_collinearity_df.Feature.sort_values().values
