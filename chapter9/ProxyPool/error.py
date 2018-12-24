# -*- coding: utf-8 -*-
# @Time    : 14.12.18 22:00
# @Author  : liu
# @Project : webSpider
# @File    : error.py
# @Software: PyCharm


class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('代理池已经枯竭')
