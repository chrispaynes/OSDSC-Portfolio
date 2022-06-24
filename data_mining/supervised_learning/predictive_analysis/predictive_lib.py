import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import display
from sklearn.ensemble import VotingClassifier
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.linear_model import LassoCV
from sklearn.metrics import (RocCurveDisplay, accuracy_score, confusion_matrix,
                             f1_score, precision_score, recall_score,
                             roc_auc_score)
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


def create_classification_metrics(y_test, y_pred, figsize=(3, 3), fontsize=12):
    c_matrix = confusion_matrix(y_test, y_pred)
    rnd = lambda v: v.round(3)

    print("Accuracy:", rnd(accuracy_score(y_test, y_pred)))
    print("Precision:", rnd(precision_score(y_test, y_pred)))
    print(
        "Recall / Sensitivity:",
        rnd(recall_score(y_test, y_pred)),
    )
    print("F1 Score:", rnd(f1_score(y_test, y_pred)))
    print("ROC-AUC Score:", rnd(roc_auc_score(y_test, y_pred)))

    plt.figure(figsize=figsize)
    plt.tight_layout()
    heatmap = sns.heatmap(
        pd.DataFrame(c_matrix), annot=True, cmap="YlGnBu", fmt="g", cbar=False
    )
    heatmap.set_xticklabels(heatmap.get_xmajorticklabels(), fontsize=fontsize)
    heatmap.set_yticklabels(heatmap.get_ymajorticklabels(), fontsize=fontsize)
    plt.title("Confusion matrix", y=1.1)
    plt.ylabel("Actual label")
    plt.xlabel("Predicted label")
    plt.show()

    return c_matrix


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


def plot_voting_classifier(
    df,
    x_cols,
    target_var,
    estimators=[
        ("DecisionTree", DecisionTreeClassifier(max_depth=4)),
        ("KNN", KNeighborsClassifier(n_neighbors=12, leaf_size=30, p=1)),
        ("SVC", SVC(gamma=0.1, kernel="rbf", probability=True)),
        ("NaiveBayes", GaussianNB()),
    ],
):

    X = df[x_cols].values
    y = df[[target_var]][target_var].values

    vc = VotingClassifier(estimators=estimators, voting="soft")

    # fit all classifiers
    for (_, clf) in estimators:
        clf.fit(X, y)

    # fit the voting classifier
    vc.fit(X, y)

    # create estimator subplots
    f, axarr = plt.subplots(1, len(estimators) + 1, figsize=(20, 10))

    # Plot decision regions
    for idx, (title, clf) in enumerate(estimators + [("VotingClassifier", vc)]):
        DecisionBoundaryDisplay.from_estimator(
            clf,
            X,
            ylabel="Tenure",
            xlabel=x_cols[0],
            alpha=0.4,
            ax=axarr[idx],
            response_method="predict",
        )

        sns.scatterplot(
            X[:, 0], X[:, 1], ax=axarr[idx], s=30, hue=df[target_var], edgecolor="k"
        )
        axarr[idx].set_title(f"{title}\nScore: {clf.score(X,y)}")

    plt.show()


def plot_error_lines(
    X_train, X_test, y_train, y_test, estimator, title="", x_label="CV Fold", xticks=[], scoring='neg_mean_absolute_error'
):
    x_points = np.arange(0, estimator.cv)

    train_accuracy = abs(cross_val_score(estimator, X_train, y_train, scoring=scoring, n_jobs=-1, cv=estimator.cv))
    test_accuracy = abs(cross_val_score(estimator, X_test, y_test, scoring=scoring, n_jobs=-1, cv=estimator.cv))
    
    summary_df = pd.DataFrame(
        {
            "# Variables": [X_train.shape[1]],
            "Train MAE": [np.round(np.mean(train_accuracy), 2)],
            "Test MAE": [np.round(np.mean(test_accuracy), 2)],
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
        line_kws={'linewidth': 1.5},
        label=f"Train MAE: {round(np.mean(train_accuracy), 2)}",
    )
    sns.regplot(
        x_points,
        y=test_accuracy,
        ci=None,        
        line_kws={'linewidth': 1.5},        
        label=f"Test MAE: {round(np.mean(test_accuracy), 2)}",
    )    

    plt.legend()
    plt.xticks(xticks or range(estimator.cv))
    plt.xlabel(x_label)
    plt.ylabel("Mean Absolute Error")
    plt.show()


def plot_param_options_accuracy(
    X_train,
    X_test,
    y_train,
    y_test,
    pipeline,
    param_grid,
    options,
    options_key,
    step,
    title = "",
    x_label = "",    
    scoring='neg_mean_absolute_error',
    param_desc=""
):
    # visualize model accuracy of test vs training data using different n_neighbors

    # Setup arrays to store train and test scores
    opts_range = np.arange(1, len(options) + 1)
    train_scores = np.empty(len(opts_range))
    test_scores = np.empty(len(opts_range))

    param_grid = param_grid or {
        'elasticNet__alpha': [1],
        'elasticNet__copy_X': [True],
        'elasticNet__fit_intercept': [True],
        'elasticNet__l1_ratio': [0.5],
        'elasticNet__max_iter': [1000],
        'elasticNet__positive': [False],
        'elasticNet__precompute': [False],
        'elasticNet__random_state': [None],
        'elasticNet__selection': ['cyclic'],
        'elasticNet__tol': [0.0001],
        'elasticNet__warm_start': [False]
    }    

    for i, k in enumerate(options):
        param_grid[f"{step}__{options_key}"] = [k]        

        cv = GridSearchCV(pipeline, param_grid=param_grid, cv=5)

        # Fit the classifier to the training data
        pipeline.fit(X_train, y_train)
        cv.fit(X_train, y_train)

        # Compute score on the training set
        train_scores[i] = np.mean(abs(cross_val_score(cv, X_train, y_train, scoring=scoring, n_jobs=-1, cv=pipeline.cv)))

        # Compute score on the testing set
        test_scores[i] = np.mean(abs(cross_val_score(cv, X_test, y_test, scoring=scoring, n_jobs=-1, cv=pipeline.cv)))       
        
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
    plt.xlabel(x_label or f"{step} {options_key} options")
    plt.ylabel("Mean Absolute Error" or scoring)
    plt.show()


def plot_ROC_curve(estimator, X_test, y_test):
    RocCurveDisplay.from_estimator(estimator, X_test, y_test, color="orange")
    plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
    plt.title("Receiver Operating Characteristic")
    plt.show()

    
from sklearn.linear_model import ElasticNetCV


def plot_elastic_net_feature_importance(X_train, y_train):
    steps = [
        ("scaler", StandardScaler()),
        ("elasticNet", ElasticNetCV()),
    ]

    pipeline = Pipeline(steps).fit(X_train, y_train)

    reg = pipeline.named_steps.get("elasticNet")

    print("Best alpha using built-in ElasticNet:", reg.alpha_)
    # coefficient of determination of the prediction.
    print("Best R2 score using built-in ElasticNet:", reg.score(X_train, y_train))
    # The amount of penalization chosen by cross validation.
    coef = pd.Series(reg.coef_, index=X_train.columns)

    selected_vars = abs(coef) > 0
    selected_cols = coef[selected_vars == True].index
    print("Lasso selected", list(selected_cols))
    num_selected_vars = sum(selected_vars)

    print(
        f"Lasso selected {num_selected_vars} variables and eliminated { sum(abs(coef) == 0) } variables"
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


def get_selected_features(X_train, cv, step_key="feature_selection"):
    return X_train.columns[cv.estimator.named_steps[step_key].get_support()]
