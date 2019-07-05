#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 11:36
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : host_parse.py
# @Software: PyCharm
import pickle


# 读取解析原始文件，返回字典
def parse_host(file):
    hostdict = {}
    with open(file, 'r') as f:
            for line in f.readlines():
                temp = line.split(',')
                hostdict[temp[1].strip()] = temp[0].strip()
    return hostdict


# 保存为文件
def save_host(dict):
    with open('example.txt', 'w') as f:
        for k, v in dict.items():
            f.writelines(f'{k} {v}\n')


# 保存为pickle
def save_pickle(file):
    with open('testpickle.data', 'wb') as f:
        pickle.dump(file, f)


# 读取pickle
def open_pickle(filename):
    with open(filename, 'rb') as f:
        list1 = pickle.load(f)
    return list1


if __name__ == '__main__':
    hosts = parse_host('d:\\file_example.txt')
    save_host(hosts)
    save_pickle(hosts)
    print(open_pickle('testpickle.data'))
