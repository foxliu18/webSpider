# -*- coding: utf-8 -*-
# @Time    : 08.12.18 10:30
# @Author  : liu
# @Project : webSpider
# @File    : tesseract_text.py
# @Software: PyCharm
import tesserocr
from PIL import Image

if __name__ == '__main__':
    image = Image.open('code2.jpg')
    image = image.convert('L')  # 'L'输出灰度图 '1'输出二值化图
    image.show()
    threshold = 166
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table, '1')
    image.show()
    result = tesserocr.image_to_text(image)
    print(result)
