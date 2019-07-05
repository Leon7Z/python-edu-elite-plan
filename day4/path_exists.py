#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 15:12
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : path_exists.py
# @Software: PyCharm
import os


def path_exists(path):
    if os.path.exists(path):
        print("111")
    else:
        print("文件不存在")

if __name__ == '__main__':
    path_exists('D:\\')
