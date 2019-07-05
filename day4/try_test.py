#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 14:56
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : try_test.py
# @Software: PyCharm
import time


def file_read(filename):
    try:
        f = open(filename, 'r')
    except Exception as e:
        print("111", e,"将在5秒后退出")
        time.sleep(5)
        exit(0)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')


if __name__ == '__main__':
    file_read("xxx")
    # try:
    #     file_read("xxx")
    # except Exception as e:
    #     print('errer', e)
