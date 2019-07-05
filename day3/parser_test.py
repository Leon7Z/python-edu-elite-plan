#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 14:33
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : parser_test.py
# @Software: PyCharm

import sys
from optparse import OptionParser


# def option():
#     # 创建一个parser对象
#     parser = OptionParser()
#     # 增加一个选项
#     parser.add_option(
#         "-f",
#         "--file",
#         action="store",
#         type="string",
#         dest="filename",
#         help="config file")
#     parser.add_option(
#         "-q",
#         "--quiet",
#         action="store_false",
#         dest="verbose",
#         default=True,
#         help="exit")
#     (options, args) = parser.parse_args()
#     # 获取参数的办法是options.变量名称，在desc=“”指定。
#     print(options.filename)
#     print(options.verbose)
#
#
# option()

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
        dest="nodename",
        help="node type")
    parser.add_option(
        '-n',
        '--hostname',
        action='store',
        type="string",
        dest="hostname",
        help="host name")
    return parser


if __name__ == '__main__':
    optpar = init_parser()
    if len(sys.argv) < 2:
        optpar.print_help()
    else:
        (options, args) = optpar.parse_args()
        print(type(options))
        print(type(optpar))
        print(options.nodename)
        print(options.hostname)
