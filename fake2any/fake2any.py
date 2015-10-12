# coding:utf-8
import sys
import argparse
from salesforce import Salesforce
from fake2csv import Csv
import yaml

parser = argparse.ArgumentParser(description='Output dammy data for any format and platform.')
#parser.add_argument('command', nargs='?', type=str, help='')
parser.add_argument('-r', '--rows', type=str, help='')
parser.add_argument('-l', '--language', type=str, help='')
parser.add_argument('-o', '--output', type=str, help='')

args = parser.parse_args()

config = yaml.load(open("config.yml", "r"))
config["args"] = args

if args.output == "salesforce" :
    plugin = Salesforce(config)
else:
    plugin = Csv(config)
plugin.load()