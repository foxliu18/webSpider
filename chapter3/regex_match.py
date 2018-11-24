#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24/024 11:32
# @Author  : foxLiu
# @File    : regex_match.py
# @Software: PyCharm

import re

if __name__ == '__main__':
    content = '''Hello 123 4567 World_This 
    is a Regex Demo'''
    print(len(content))
    result = re.match('^He.*?(\d+).*?Demo', content, re.S)
    print(result, '\n')
    if result is not None:
        print(result.group(1))
        print(result.groups(), '\n')
        print(result.span())
