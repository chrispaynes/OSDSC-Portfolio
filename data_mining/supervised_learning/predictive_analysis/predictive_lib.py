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
from sklearn.model_selection import GridSearchCV
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


def plot_accuracy_lines(
    X_train, X_test, y_train, y_test, cv, title="", x_label="", xticks=[]
):
    x_points = [0, 1]

    train_accuracy = cv.score(X_train, y_train)
    test_accuracy = cv.score(X_test, y_test)

    summary_df = pd.DataFrame(
        {
            "# Variables": [X_train.shape[1]],
            "Train Acc.": [train_accuracy],
            "Test Acc.": [test_accuracy],
            "Best Model Params": [cv.best_params_],
        }
    )

    try:
        important_feats = X_train.columns[
            cv.estimator["feature_selection"].get_support()
        ]
        summary_df["Imp. Feats."] = [list(important_feats)]
        summary_df["# Imp. Feats."] = [len(important_feats)]
    except:
        # ignore errors when there's no 'feature_selection' step
        pass

    display(summary_df)

    plt.figure(figsize=(10, 5))
    plt.title(title)
    plt.plot(
        x_points,
        [train_accuracy] * 2,
        label=f"Training Accuracy: {round(train_accuracy, 2)}",
    )
    plt.plot(
        x_points, [test_accuracy] * 2, label=f"Test Accuracy: {round(test_accuracy, 2)}"
    )
    plt.legend(loc="center left")
    plt.xticks(xticks)
    plt.xlabel(x_label)
    plt.ylabel("Accuracy")
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
    title,
    x_label,
):
    # visualize model accuracy of test vs training data using different n_neighbors

    # Setup arrays to store train and test accuracies
    neighbors = np.arange(1, len(options) + 1)
    train_accuracy = np.empty(len(neighbors))
    test_accuracy = np.empty(len(neighbors))

    param_grid = param_grid or {
        "imp__strategy": ["mean"],
        "knn__n_neighbors": [5, 10, 15, 20, 25],
        "knn__weights": ["uniform", "distance"],
        "knn__leaf_size": [30],
        "knn__p": np.arange(1, 3),
    }

    for i, k in enumerate(options):
        param_grid[options_key] = [k]

        cv = GridSearchCV(pipeline, param_grid=param_grid, cv=5)

        # Fit the classifier to the training data
        pipeline.fit(X_train, y_train)
        cv.fit(X_train, y_train)

        # Compute accuracy on the training set
        train_accuracy[i] = cv.score(X_train, y_train)

        # Compute accuracy on the testing set
        test_accuracy[i] = cv.score(X_test, y_test)

        # print("Best Estimator", cv.best_estimator_)
        print("Best Params", cv.best_params_)
        try:        
            print(
                "feature_importances_",
                X_train.columns[pipeline["feature_selection"].get_support()],
            )
        except:
            # ignore errors when there's no 'feature_selection' step
            pass            

    plt.title(title)
    plt.plot(options, test_accuracy, label="Testing Accuracy")
    plt.plot(options, train_accuracy, label="Train Accuracy")
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel("Accuracy")
    plt.show()


def plot_ROC_curve(estimator, X_test, y_test):
    RocCurveDisplay.from_estimator(estimator, X_test, y_test, color="orange")
    plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
    plt.title("Receiver Operating Characteristic")
    plt.show()


def plot_lasso_feature_importance(X_train, y_train):
    steps = [
        ("scaler", StandardScaler()),
        ("lasso", LassoCV()),
    ]

    pipeline = Pipeline(steps).fit(X_train, y_train)

    reg = pipeline.named_steps.get("lasso")

    print("Best alpha using built-in LassoCV:", reg.alpha_)
    # coefficient of determination of the prediction.
    print("Best score using built-in LassoCV:", reg.score(X_train, y_train))
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
    barplot.set_title("Lasso Model Feature Importance")

    imp_coef[abs(imp_coef["Feature Importance"]) > 0]
    
    plt.show()

    return list(selected_cols)


def get_selected_features(X_train, cv, step_key="feature_selection"):
    return X_train.columns[cv.estimator.named_steps[step_key].get_support()]
