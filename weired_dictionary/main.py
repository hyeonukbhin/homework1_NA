#!/usr/bin/python3

import configparser

import weired_dictionary.tools.dictionary as wd_tool

config = configparser.ConfigParser()
config.read('config.cfg')
PATH = config['DEFAULT']['PATH']
FILENAME = config['DEFAULT']['FILENAME']
INIT_DATA = bool(int(config['DEFAULT']['INIT_DF']))


def main():
    if INIT_DATA is True:
        wd_tool.init_dict()
    while True:
        print("=============================================")
        print("      Welcome to Weird Dictionary (WD)!      ")
        print("1. Show all words in WD")
        print("2. Add a new word to WD")
        print("3. Remove some word from WD")
        print("4. Update some word from WD")
        print("5. Close WD")
        print("=============================================")
        selection = input("Choose what you want to do? : ")

        if selection == '1':
            wd_tool.show_dict()
        elif selection == '2':
            key = input("Fill in a item you want to add? : ")
            value = input("Fill in a description of the item you want to add? :")
            wd_tool.add_dict(key, value)
        elif selection == '3':
            wd_tool.show_dict()
            key = input("Fill in the item you want to remove? : ")
            print(wd_tool.check_index(key))
            if wd_tool.check_index(key) is True:
                wd_tool.remove_dict(key)
            else:
                print("There are information : {} in the dictionary.".format(key))
        elif selection == '4':
            key = input("Fill in the item you want to update? : ")
            if wd_tool.check_index(key) is True:
                wd_tool.check_index(key, value)
                value = input("Fill in a description of the item you want to add? :")
            else:
                print("There are information : {} in the dictionary.".format(key))
        else:
            print("\nGood Bye.")
            break

        input("Press Enter to continue...")


main()
