#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25/025 23:58
# @Author  : Liu
# @File    : bs4_method.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import re

html = """
    <div class="panel">
    <div class="panel-heading">
    <h4>Hello</4>
    </div>
    <div class="panel-body">
    <ul class="list" id="list-1" name="elements">
    <li class="element">Foo
    <a>Hello, this is a link</a>
    <a>Hello, this is a link, too</a>
    </li>
    <li class="element">Bar</li>
    <li class="element">Jay</li>
    </ul>
    <ul class="list list-small" id="list-2">
    <li class="element">Foo</li>
    <li class="element">Bar</li></ul>
    </div>
    </div>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html, "lxml")

    print(soup.find_all(name='ul'), '\n')
    print(type(soup.find_all(name='ul')[0]), '\n')
    print(len(soup.find_all(name='ul')), '\n')

    for ul in soup.find_all(name='ul'):
        print(ul.find_all(name='li'))
        for li in ul.find_all(name='li'):
            print(li.string)

    print('\n')
    print(soup.find_all(attrs={'id': 'list-2'}), '\n')
    print(soup.find_all(attrs={'name': 'elements'}), '\n')
    print(soup.find_all(class_="element"), '\n')

    print(soup.find_all(text=re.compile('link')), '\n')

    print('new', '\n')
    print(soup.find(name='ul'), '\n')
    print(soup.find(name='li'), '\n')
    print(type(soup.find(name='li')), '\n')
    print(soup.find(class_='list-small'), '\n')

    print(soup.find_parent(name='li'), '\n')

    print(soup.select('.panel .panel-heading'), '\n')
    print(soup.select('ul li'), '\n')
    print(soup.select('#list-2 .element'), '\n')
    print(type(soup.select('ul')[0]))
