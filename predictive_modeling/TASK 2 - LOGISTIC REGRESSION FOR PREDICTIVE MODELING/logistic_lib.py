import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math

from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import RFE
from sklearn.feature_selection import RFECV
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn import metrics

import scikitplot as skplt

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

sigmoid = lambda x: 1 / (1 + math.exp(-x))


def reset_cols(data, target_var):
    y_col = [target_var]
    x_cols = data.columns[~data.columns.isin(y_col)]

    return y_col, x_cols


def create_vif_dataframe(data, x_cols):
    VIFS = {
        col: variance_inflation_factor(data[x_cols].values, i).round(3)
        for i, col in enumerate(x_cols)
    }

    VIF_df = pd.DataFrame({"Feature": VIFS.keys(), "VIF": VIFS.values()}).sort_values(
        by="VIF", ascending=False
    )
    VIF_df.style.hide_index()

    return VIF_df


def filter_high_vif_features(VIF_data, VIF_threshold=5):
    low_collinearity_df = VIF_data[VIF_data.VIF < VIF_threshold]

    return low_collinearity_df.Feature.sort_values().values


def plot_feature_cross_val_scores(min_num_features, model):
    plt.plot(
        range(min_num_features, len(model.grid_scores_) + min_num_features),
        model.grid_scores_,
    )

    plt.xticks(np.arange(0, len(model.grid_scores_) + 1, step=1))
    plt.xlabel("# Selected Features")
    plt.ylabel("Cross Validation Score (Accuracy)")
    plt.show()


def predict_log_odds(
    Complication_Risk_Low, Initial_Admin_Emergency_Admission, Initial_Days
):
    intercept = -21.5604
    B1 = -0.4576
    B2 = 0.7642
    B3 = 28.5984

    equation = (
        intercept
        + (B1 * Complication_Risk_Low)
        + (B2 * Initial_Admin_Emergency_Admission)
        + (B3 * Initial_Days)
    )
    y = round(equation, 2)

    return y


def standardize_data(data, x_cols):
    standard_df = data.copy()
    standard_df[x_cols] = StandardScaler().fit_transform(standard_df[x_cols])

    return standard_df


def split_data(data, target_var, x_cols):
    sm = SMOTE(random_state=1)

    x_train, x_test, y_train, y_test = train_test_split(
        data[x_cols], data[target_var], test_size=0.33, random_state=1
    )

    # The correct application of oversampling during k-fold cross-validation is to apply the method
    # to the training dataset only, then evaluate the model on the stratified but non-transformed test set.
    sm = SMOTE(random_state=1).fit(x_train, y_train)
    under = RandomUnderSampler(random_state=1).fit(x_train, y_train)

    steps = [("over-sampler", sm), ("under-sampler", under)]
    pipeline = Pipeline(steps=steps)
    x_train, y_train = pipeline.fit_resample(x_train, y_train)

    return x_train, x_test, y_train, y_test


def create_heatmap(data, title="DataFrame Correlation Heatmap"):
    plt.figure(figsize=(50, 40))

    mask = np.triu(np.ones_like(data.corr(), dtype=bool))

    heatmap = sns.heatmap(
        data.corr(),
        mask=mask,
        vmin=-1,
        vmax=1,
        annot=True,
        annot_kws={"fontsize": 24},
        fmt=".2f",
    )
    heatmap.set_xticklabels(heatmap.get_xmajorticklabels(), fontsize=48)
    heatmap.set_yticklabels(heatmap.get_ymajorticklabels(), fontsize=48)
    heatmap.set_title(title, fontdict={"fontsize": 75}, pad=2)


def create_conf_matrix(y_test, y_pred):
    c_matrix = metrics.confusion_matrix(y_test, y_pred)
    rnd = lambda v: v.round(3)

    sns.heatmap(pd.DataFrame(c_matrix), annot=True, cmap="YlGnBu", fmt="g")
    plt.title("Confusion matrix", y=1.1)
    plt.ylabel("Actual label")
    plt.xlabel("Predicted label")

    print("Accuracy:", rnd(metrics.accuracy_score(y_test, y_pred)))
    print("Precision:", rnd(metrics.precision_score(y_test, y_pred)))
    print(
        "Recall / Sensitivity:",
        rnd(metrics.recall_score(y_test, y_pred)),
    )
    print("F1 Score:", rnd(metrics.f1_score(y_test, y_pred)))
    print("ROC-AUC Score:", rnd(metrics.roc_auc_score(y_test, y_pred)))
    print("Confusion Matrix:")
    print(c_matrix)

    plt.show()


def visualize_log_model(model, data, x, y, intercept, slope):
    sns.regplot(x=x, y=y, data=data, ci=None, logistic=True)
    plt.axline(xy1=(0, intercept), slope=slope, color="black")
    plt.show()


def plot_cumulative_gains_curve(
    x_train, x_test, y_train, y_test, title="Cumulative Gains Curve"
):
    lr = LogisticRegression().fit(x_train, y_train)

    y_probas = lr.predict_proba(x_test)
    skplt.metrics.plot_cumulative_gain(y_test, y_probas, title=title, figsize=(5, 5))
    plt.show()


def plot_ROC_curve(x_test, y_test):
    lr = linear_model.LogisticRegression().fit(x_test, y_test)
    y_pred_proba = lr.predict_proba(x_test)[:, 1]
    # false and true positive rates
    fpr, tpr, _ = metrics.roc_curve(y_true=y_test, y_score=y_pred_proba)

    auc = metrics.roc_auc_score(y_true=y_test, y_score=y_pred_proba)

    plt.plot(fpr, tpr, label="auc=" + str(round(auc, 2)))
    plt.legend(loc=4)
    plt.show()

    return round(auc, 2)


def get_regression(
    x_train,
    x_test,
    y_train,
    y_test,
    print_scores=True,
    print_cmatrix=True,
    print_summary=True,
):
    rnd = lambda x: x.round(3)
    stars = "*" * 5

    lr = LogisticRegression().fit(x_train, y_train)

    y_test_pred = lr.predict(x_test)
    y_train_pred = lr.predict(x_train)

    coefs_df = pd.DataFrame(lr.coef_[0], columns=["Coefficients"])
    coefs_df.index = x_train.columns

    if print_summary:
        display(coefs_df)
        print("Intercept:", rnd(*lr.intercept_))

    if print_scores:
        print(f"\n{stars} TRAINING DATA SCORE {stars}")
        print(rnd(lr.score(x_train, y_train)))

        if print_cmatrix:
            create_conf_matrix(y_train, y_train_pred)

        print(f"\n{stars} TEST DATA SCORE {stars}")
        print(rnd(lr.score(x_test, y_test)))

        if print_cmatrix:
            create_conf_matrix(y_test, y_test_pred)

        y_probas = lr.predict_proba(x_test)
        skplt.metrics.plot_cumulative_gain(y_test, y_probas)
        plt.show()

        plot_ROC_curve(x_test, y_test)

    return lr, y_train_pred, y_test_pred


def plot_cumulative_gains_curve(
    x_train, x_test, y_train, y_test, title="Cumulative Gains Curve"
):
    lr = LogisticRegression().fit(x_train, y_train)

    y_probas = lr.predict_proba(x_test)
    skplt.metrics.plot_cumulative_gain(y_test, y_probas, title=title, figsize=(10, 5))
    plt.show()


def plot_lift_curve(x_train, x_test, y_train, y_test, title="Lift Curve"):
    lr = LogisticRegression().fit(x_train, y_train)
    x_train

    # The returned estimates for all classes (0, 1) are ordered by the label of classes.
    y_probas = lr.predict_proba(x_test)

    skplt.metrics.plot_lift_curve(y_test, y_probas, title=title, figsize=(10, 5))
    plt.show()


def plot_feature_cross_val_scores(min_num_features, model):
    plt.plot(
        range(min_num_features, len(model.grid_scores_) + min_num_features),
        model.grid_scores_,
    )

    plt.xticks(np.arange(0, len(model.grid_scores_) + 1, step=1))
    plt.xlabel("# Selected Features")
    plt.ylabel("Cross Validation Score (Accuracy)")
    plt.show()
