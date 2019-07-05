#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 16:02
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : hosts_get_ipddr.py
# @Software: PyCharm

import configparser
import os
import sys
from optparse import OptionParser


# 初始化
def init_parser():
    # 修改默认提示
    usage = "%prog [options]... [files]...\nexample: %prog -t node -n linux-node1"
    # 创建一个parser对象
    parser = OptionParser(usage=usage)
    # 添加option内容
    parser.add_option(
        '-t',
        '--type',
        action='store',
        type="string",
        dest="nodetype",
        help="node type")
    parser.add_option(
        '-n',
        '--hostname',
        action='store',
        type="string",
        dest="hostname",
        help="host name")
    return parser


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
    optpar = init_parser()
    (options, args) = optpar.parse_args()
    print(len(sys.argv))
    if len(sys.argv) < 2:
        optpar.print_help()
    elif len(sys.argv) == 3:
        lookup_ipaddr(options.hostname)
    elif len(sys.argv) == 5:
        lookup_ipaddr(options.hostname, options.nodetype)
    else:
        optpar.print_help()
