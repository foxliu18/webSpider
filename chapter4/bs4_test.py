#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25/025 22:31
# @Author  : Liu
# @File    : bs4_test.py
# @Software: PyCharm

from bs4 import BeautifulSoup

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dormouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="https://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="https://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="https://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """

if __name__ == '__main__':
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title)
    print(type(soup.title))
    print(soup.title.string)
    print(soup.head.title)
    print(soup.a.contents)
