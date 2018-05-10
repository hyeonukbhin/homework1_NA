#!/usr/bin/python3

import configparser

import pandas as pd
import weired_dictionary.tools.dataframe as df_tool

config = configparser.ConfigParser()
config.read('config.cfg')
FILEPATH = config['DEFAULT']['FILEPATH']


def init_dict():
    index = ["사과", "딸기", "포도", "바나나"]
    # columns = ['price', 'stock']
    raw_data = {"의미": ["빨간색 과일", "빨간색 씨가 달린 과일", "보라색 송이송이 과일", "노란색 길쭉한 과일"]}
    df = pd.DataFrame(raw_data, index=index)
    df_tool.save_df(df, FILEPATH)


def show_dict():
    print("=============================================")
    df = df_tool.read_df(FILEPATH)
    print(df)
    print("=============================================")


def add_dict(key, value):
    index = key
    df = df_tool.add_df(index, "의미", value)
    df_tool.save_df(df, FILEPATH)


def update_dict(key, value):
    index = key
    df = df_tool.update_df(index, "의미", value)
    df_tool.save_df(df, FILEPATH)


def remove_dict(key):
    index = key
    df = df_tool.remove_row_df(index)
    df_tool.save_df(df, FILEPATH)


def check_dict(key):
    index = key
    df = df_tool.check_index(index)
    print(df)


def check_index(key=None):
    index = key
    index_list = df_tool.get_indexlist()
    if index is None:
        print(index_list)
        result = False
    else:
        result = index in index_list
    return result

# print(check_index("바나나"))
