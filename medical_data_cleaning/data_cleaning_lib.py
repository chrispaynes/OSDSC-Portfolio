import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


def create_boxplots(df):
    # create a histogram for numerical columns    
    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        fig = plt.figure(figsize=(19, 1.5))
        _ = sns.boxplot(x=col, data=df, labels=[col], orient="h")
        plt.show()


def create_histograms(df):
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    fig, axes = plt.subplots(len(numeric_cols), 1, figsize=(15, 50))

    # create a histogram for numerical columnsgi
    rounded_df = df.round()
    for ax, col in zip(axes, numeric_cols):
        ax.set_title(col)
        _ = sns.histplot(data=rounded_df, x=col, ax=ax, kde=True)

    fig.tight_layout(pad=2.0)
    plt.show()


def create_hist_and_boxplots(df, col):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(25, 5))
    sns.histplot(data=df, x=col, ax=axes[0], binwidth=1, discrete=True)
    sns.boxplot(data=df, x=col, ax=axes[1])


def plot_categorical_counts(df, cols):
    fig, axes = plt.subplots(len(cols) // 3, 3, figsize=(30, 30))
    axes = axes.flatten()

    for ax, c in zip(axes, cols):
        try:
            sns.countplot(data=df, y=c, ax=ax)
        except Exception as e:
            print(f"error creating countplot for {c}", e)

    fig.tight_layout(pad=0.5)


def create_category_encodings(df):
    encodings = {}
    encoded_df = df.copy()
    ctg_cols = df.select_dtypes(include=["category"]).columns

    for col in ctg_cols:
        le = LabelEncoder()
        cats = df[col].unique()
        le.fit(cats)
        encodings[col] = le
        encoded_df[col] = le.transform(encoded_df[col])
        print(f"category: {col} succesfully encoded")

    return encodings, encoded_df, ctg_cols


def write_encodings_csv(encodings):
    encodings_dict = {}

    for k, v in encodings.items():
        encodings_dict[k] = {}
        for index, c in enumerate(v.classes_):
            encodings_dict[k][index] = c

    output_df = pd.DataFrame.from_dict(encodings_dict, orient="index")
    output_df.index.name = "feature"
    output_df.to_csv("encodings.csv", index=True)


def create_na_mask(df, pct):
    return df.isna().sum() / len(df) < pct
