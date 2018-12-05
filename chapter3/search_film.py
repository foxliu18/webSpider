#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/24/024 22:43
# @Author  : foxLiu
# @File    : search_film.py
# @Software: PyCharm

import requests
import re
import json
import time
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_13_3 '
                          'AppleWebKit/537.36(KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html_text = get_one_page(url)
    for item in parse_one_page(html_text):
        print(item)
        write_to_file(item)


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)'
        '</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?'
        'fraction.*?>(.*?)</i>.*?</dd>', re.S
    )
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2].strip(),
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5].strip() + item[6].strip()
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':

    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
