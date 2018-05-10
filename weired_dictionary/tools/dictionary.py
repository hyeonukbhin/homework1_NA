#!/usr/bin/python3
#-*- coding: utf-8 -*-

import tools.dataframe as df_tool
import numpy as np
import pandas as pd
#
# Welcome to Weird Dictionary (WD)!
# 1. Show all words in WD
# 2. Add a new word to WD
# 3. Remove some word from WD 4. Close WD
# Choose what you want to do?:1 WD is empty.

def init_dict():
    index = ["사과", "딸기", "포도", "바나나"]
    # columns = ['price', 'stock']
    raw_data = {"의미": ["빨간색 과일", "빨간색 씨가 달린 과일", "보라색 송이송이 과일", "노란색 길쭉한 과일"]}
    df = pd.DataFrame(raw_data, index=index)
    df_tool.save_df(df, "Data.csv")

def show_dict():
    print("=============================================")
    df = df_tool.read_df("Data.csv")
    print(df)
    print("=============================================")

def add_dict(key, value):
    index = key
    df = df_tool.add_df(index, "의미", value)
    df_tool.save_df(df)

def update_dict(key, value):
    index = key
    df = df_tool.update_df(index, "의미", value)
    df_tool.save_df(df, "Data.csv")

def remove_dict(key):
    index = key
    df = df_tool.remove_row_df(index)
    df_tool.save_df(df, "Data.csv")

def start_section():
    print("=============================================")
    print("      Welcome to Weird Dictionary (WD)!      ")
    print("1. Show all words in WD")
    print("2. Add a new word to WD")
    print("3. Remove some word from WD 4. Close WD")
    print("=============================================")
    selection = input("Choose what you want to do? : ")

    if selection == '1':
        show_dict()
    elif selection == '2':
        add_dict()
    elif selection == '3':
        remove_dict()
    else:
        print("\n INVALID SELECTION \n")"

def end_section():

def pop_items(order):
    print("{} 상품이 나왔습니다.".format(order))
    df_tool.sale_item(order)

def pop_change(change):
    print("잔돈 {}원이 나왔습니다.".format(change))