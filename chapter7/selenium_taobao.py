# -*- coding: utf-8 -*-
# @Time    : 06.12.18 22:56
# @Author  : liu
# @Project : webSpider
# @File    : selenium_taobao.py
# @Software: PyCharm
from urllib.parse import quote

import pymongo
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome()
# browser1 = webdriver.Firefox()
wait = WebDriverWait(browser, 15)
KEYWORD = 'iPad'


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            eingabe = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pagerd div.form > spn.btn.J_Submit'))
            )
            eingabe.clear()
            eingabe.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


MONGO_UEL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_UEL)
db = client[MONGO_DB]


def save_to_mongo(result):
    """
    保存至MongoDB
    :param result: 结果
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功')
    except Exception as e:
        print('Error:', e.args[1])
        print('存储到MongoDB失败')


if __name__ == '__main__':
    MAX_PAGE = 1
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
