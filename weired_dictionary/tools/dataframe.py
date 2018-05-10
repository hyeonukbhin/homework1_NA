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
        df = read_df('Data.csv')
    df = df.copy()

    pre_value = df.loc[index, columns]
    df.loc[index, columns] = post_value
    print("{} : {} of {} is updated to {}".format(columns, pre_value, index, post_value))
    return df

def add_df(index, columns, init_value, df=None):
    if df is None:
        df = read_df('Data.csv')
    df.loc[index, columns] = init_value
    print("{} : {} of {} is added.".format(columns, init_value, index))
    return df

def remove_row_df(index, df=None):
    if df is None:
        df = read_df('Data.csv')
    df.drop([index])
    print("row : {} is removed.".format(index))
    return df

def check_df(index, columns, df=None):
    if df is None:
        df = read_df('Data.csv')
    result = df[columns][index]
    return result