#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: ZHU Cenzhe, Davy
# Email: cenzhe.zhu@gmail.com
# Description: 
# Creation time: Thu Dec 11 11:42:42 CST 2014

import sys
import json
import urllib
from collections import defaultdict

# sample input:
# /api/fuzzy_search?callback=jQuery1720058342891512438655_1417449691204&from=%E6%88%90%E9%83%BD&to=%E5%A4%A7%E4%B8%98&fromDate=2014-12-03&toDate=2015-11-27&flightType=1&_=1417449691223
def parse(line, argv):
    data = defaultdict(str)
    i, start, flag = 0, 0, 0
    search, key, token = '?', '', ''
    for ch in line:
        if ch == search:
            if start != 0:
                token = line[start:i]
                if flag == 0:
                    key = token
                    search = '&'
                else:
                    data[key] = urllib.unquote(token)
                    search = '='
                flag = 1 - flag
            else:
                search = '='
            start = i+1
        i = i+1
    # append the last key-value pair
    data[key] = urllib.unquote(line[start:-1])
    out = []
    for i in range(1, len(argv)):
        out.append(data[argv[i]])
    print(','.join(out))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: cat somefile | ./param_parse.py fields_to_extract")
        sys.exit(0)
    for line in sys.stdin:
        data = parse(line, sys.argv)
