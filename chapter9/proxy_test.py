# -*- coding: utf-8 -*-
# @Time    : 14.12.18 20:32
# @Author  : liu
# @Project : webSpider
# @File    : proxy_test.py
# @Software: PyCharm
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

import requests


def urllib_proxy():
    proxy = '113.116.145.136:9000'
    proxy_handler = ProxyHandler({
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    })
    opener = build_opener(proxy_handler)
    try:
        response = opener.open('http://httpbin.org/get')
        print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)


def requests_proxy():
    proxy = '113.116.145.136:9000'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


if __name__ == '__main__':
    requests_proxy()
