#!/usr/bin/python3
#-*- coding: utf-8 -*-

import numpy as np
import pandas as pd



def save_df(df, filename):
    df.to_csv(filename, sep=',')


def read_df(filename):
    df = pd.read_csv(filename, sep=',', na_values=".", index_col=0)
    return df


def update_df(index, columns, post_value, df=None):
    if df is None:
        df = read_df('Beverage.csv')
    df = df.copy()

    pre_value = df.loc[index, columns]
    df.loc[index, columns] = post_value
    print("{} {} of {} is updated to {}".format(columns, pre_value, index, post_value))
    return df


def check_df(index, columns, df=None):
    if df is None:
        df = read_df('Beverage.csv')
    result = df[columns][index]
    return result



def sale_item(index, df=None):
    if df is None:
        df = read_df('Beverage.csv')
    df = df.copy()
    columns = "stock"
    # pre_value = df[columns][index]
    pre_value = df.loc[index, columns]
    # print("ttttttttttt")
    # print(tools)
    post_value = pre_value - 1
    df.loc[index, columns] = post_value
    if post_value == 0:
        df.loc[index, "available"] = "X"
        # df["available"][index] = "X"

    save_df(df, "Beverage.csv")
    return df
