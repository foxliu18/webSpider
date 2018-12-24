#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 23.12.18 21:44
# @Author  : liu
# @Project : webSpider
# @File    : run.py
# @Software: PyCharm
from chapter9.WeChat.spider import Spider

if __name__ == '__main__':
    spider = Spider()
    spider.run()
