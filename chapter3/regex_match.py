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
    result = re.match('^He.*?(\d+).*?Demo', content, re.S)
    if result is None:
        print(len(content))
        print(result, '\n')
        print(result.group(1))
        print(result.groups(), '\n')
        print(result.span())

    content_trans = '(百度)www.baidu.com'
    result_trans = re.match('\(百度\)www.baidu.com', content_trans)
    if result_trans is None:
        print(result_trans)

    # match()从头开始匹配，一旦开头不匹配，直接None
    # search()扫描整个字符串
    content_search = 'Extra string Hello 1234567 World_This is a Regex Demo Extra strings'
    result_search = re.search('Hello.*?(\d+).*?Demo', content_search)
    if result_search is not None:
        print(result_search)
        print(result_search.group())
        print(result_search.groups())
