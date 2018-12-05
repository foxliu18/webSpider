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
    print(browser.get_cookie())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(browser.get_cookie())
    browser.delete_all_cookies()
    print(browser.get_cookies())


if __name__ == '__main__':
    cookies_operation()
    browser.close()

