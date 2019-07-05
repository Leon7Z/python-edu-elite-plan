#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 9:46
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : hosts_manage.py
# @Software: PyCharm

'''
python config_test.py *   请显示所有主机的IP地址
python config_test.py linux-node2  请显示该主机的IP地址
python config_test.py xxx   如果该主机不存在配置中，请提示我
'''

import configparser
import os
import sys


# 读取主机IP
def lookup_ipaddr(target, node_type = 'node', config_file = 'config.ini'):
    base_dir = r'C:\Users\zxleo\PycharmProjects\python-edu\day3'
    path = os.path.join(base_dir, config_file)
    conf = configparser.ConfigParser()  # 定义一个对象接收
    conf.read(path)
    if node_type == 'node':
        if target == '*':
            all_sections = conf.sections()
            for hostname in all_sections:
                print(conf[hostname]['ipaddr'], end=' ')
            exit(0)
        elif conf.has_section(target):
            print(conf[target]['ipaddr'])
            exit(0)
        else:
            print('该主机不存在配置中')
    elif node_type == 'group':
        if conf.has_option('nodegroup', target):
            group_list = conf['nodegroup'][target]
            for node in group_list.split(','):
                print(node.strip(), end=' ')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        lookup_ipaddr(sys.argv[2], sys.argv[1])
    elif len(sys.argv) == 2:
        lookup_ipaddr(sys.argv[1])
    else:
        print("Usage: python hosts_manage.py hostname")