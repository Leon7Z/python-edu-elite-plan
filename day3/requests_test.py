#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 16:29
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : requests_test.py
# @Software: PyCharm
import requests
import sys
from optparse import OptionParser


def get_ip_info(ipaddr):
    print(ipaddr)
    r = requests.get('http://freeapi.ipip.net/' + ipaddr)
    print(r.text)


def init_parser():
    # 修改默认提示
    usage = "%prog [options]... [ipaddr]...\nexample: %prog -i 192.168.1.1"
    # 创建一个parser对象
    parser = OptionParser(usage=usage)
    # 添加option内容
    parser.add_option(
        '-i',
        '--ip',
        action='store',
        type="string",
        dest="ipaddr",
        help="ipaddr")
    return parser


if __name__ == '__main__':
    optpar = init_parser()
    if len(sys.argv) < 2:
        optpar.print_help()
    else:
        (options, args) = optpar.parse_args()
        get_ip_info(options.ipaddr)

