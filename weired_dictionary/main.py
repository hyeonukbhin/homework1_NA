#!/usr/bin/python3
#-*- coding: utf-8 -*-

import tools.machine as mc_tool

def main():
    mc_tool.init_stock()
    while True:
        mc_tool.show_items()
        result_order, order = mc_tool.get_order()
        result_cash, change = mc_tool.get_cash(order)
        if (result_order == True) and (result_cash == True):
            mc_tool.pop_items(order)
            mc_tool.pop_change(change)
        else:
            print("잘못된 주문입니다.")

if __name__ == "__main__":
    main()
