#!/bin/python

import simplejson as json

from pprint import pprint

json_data = open('1line.txt')

data = json.load(json_data)

pprint(data)

json_data.close()