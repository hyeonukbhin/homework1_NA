import numpy as np
import sys
import pandas as pd


def save_df(df, filename):
    df.to_csv(filename, sep=',')


def read_df(filename):
    df = pd.read_csv(filename, sep=',', na_values=".", index_col=0)
    return df


def update_df(index, columns, post_value, df=None):
    if df is None:
        df = read_df('beverage.csv')
    pre_value = df[columns][index]
    df[columns][index] = post_value
    print("{} {} of {} is updated to {}".format(columns, pre_value, index, post_value))
    return df


def sale_item(index, df=None):
    if df is None:
        df = read_df('beverage.csv')
    columns = "stock"
    pre_value = df[columns][index]
    post_value = df[columns][index] = pre_value - 1
    if post_value == 0:
        df["available"][index] = "X"
    return df
