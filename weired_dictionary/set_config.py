#!/usr/bin/python3

import configparser
import os

PATH = os.path.dirname(os.path.abspath(__file__))
FILENAME = 'Data.csv'
FILEPATH = os.path.join(PATH, FILENAME)

config = configparser.ConfigParser()
section1 = config['DEFAULT']
section1['PATH'] = PATH
section1['FILENAME'] = FILENAME
section1['FILEPATH'] = FILEPATH
section1['INIT_DF'] = "1"

with open('config.cfg', 'w') as configfile:
  config.write(configfile)

# config.sections()
# a = config['DEFAULT']['PATH']
# b = config['DEFAULT']['FILENAME']
