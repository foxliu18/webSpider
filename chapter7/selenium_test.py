# -*- coding: utf-8 -*-
# @Time    : 05.12.18 20:54
# @Author  : liu
# @Project : webSpider
# @File    : selenium_test.py
# @Software: PyCharm
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
url_zhihu = 'https://www.zhihu.com/explore'
url_taobao = 'https://www.taobao.com/'
url_baidu = 'https://www.baidu.com/'
url_python = 'https://python.org'


def implied_wait():
    browser.implicitly_wait(10)
    browser.get(url_zhihu)
    eingabe = browser.find_element_by_class_name('zu-top-add-question')
    print(eingabe)


def explicit_wait():
    browser.get(url_taobao)
    wait = WebDriverWait(browser, 10)
    eingabe = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    print(eingabe, button)


def back_forward_action():
    browser.get(url_taobao)
    browser.get(url_zhihu)
    browser.back()
    time.sleep(2)
    browser.forward()


def cookies_operation():
    browser.get(url_zhihu)
    print('1\n', browser.get_cookies()[0])
    browser.add_cookie({'name': 'fox', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print('2\n', browser.get_cookies()[0])
    browser.delete_all_cookies()
    print('3\n', browser.get_cookies())


def window_tag_operation():
    browser.get(url_baidu)
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get(url_taobao)
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get(url_python)


if __name__ == '__main__':
    window_tag_operation()
    browser.close()

