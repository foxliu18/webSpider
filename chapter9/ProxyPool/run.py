# -*- coding: utf-8 -*-
# @Time    : 18-12-15 下午9:03
# @Author  : liu
# @Project : webSpider
# @File    : run.py
# @Software: PyCharm
from chapter9.ProxyPool.scheduler import Scheduler
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    try:
        s = Scheduler()
        s.run()
    except Exception as e:
        print('Error', e.args)
        main()


if __name__ == '__main__':
    main()
