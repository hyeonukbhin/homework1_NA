#!/usr/bin/python3

import numpy as np
import random
import vm_modules.management as mg
import pandas as pd

# index = ["Pepchi", "KokeKola", "Starblues Caffe Latte", "Bottle Water"]
# # columns = ['price', 'stock']
# raw_data = {"price": [500, 550, 1000, 300],
#             "stock": [10, 10, 25, 20],
#             "available": ["O", "O", "O", "O"]}
#
# df = pd.DataFrame(raw_data, index=index)
# print(df)
# mg.save_df(df, "beverage.csv")

df = mg.read_df("beverage.csv")
print(df)

df = mg.update_df("Pepchi", "stock", 2, df)
print(df)

df = mg.sale_item("Pepchi", df)
print(df)

df = mg.sale_item("Pepchi", df)
print(df)

# def main():
#     while (1):
#          = input("Rock or Paper or Scissor?: ")
#         correct_set = ["Rock", "Paper", "Scissor"]
#         #         print(input_user)
#         if input_user in correct_set:
#             result = function(input_user)
#             print(result)
#         else:
#             print("not correct")

#
# if __name__ == "__main__":
#     main()
