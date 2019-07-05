#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 16:04
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : ssh_test.py
# @Software: PyCharm
import paramiko
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


def read_config(target, node_type='node', config_file = 'hosts.ini'):
    base_dir = r'C:\Users\zxleo\PycharmProjects\python-edu\day4'
    path = os.path.join(base_dir, config_file)
    conf = configparser.ConfigParser()  # 定义一个对象接收
    conf.read(path)
    if node_type == 'node':
        if target == '*':
            all_sections = conf.sections()
            ipaddr = []
            passwd = []
            host = []
            for hostname in all_sections:
                if hostname == 'nodegroup':
                    continue
                host.append(hostname)
                ipaddr.append(conf[hostname]['ipaddr'])
                passwd.append(conf[hostname]['password'])
            return ipaddr, passwd, host
            exit(0)
        elif conf.has_section(target):
            ipaddr = conf[target]['ipaddr']
            passwd = conf[target]['password']
            return ipaddr, passwd, target
        else:
            print('该主机不存在配置中')
            exit(0)
    elif node_type == 'group':
        if conf.has_option('nodegroup', target):
            group_list = conf['nodegroup'][target]
            for node in group_list.split(','):
                print(node.strip(), end=' ')


'''
可以改为class，把函数变为类函数
'''


# ssh连接
def ssh_connect(passwd, ipaddr, user='root', port=22):
    # 创建Paramiko的SSH对象
    ssh = paramiko.SSHClient()
    # 访问未知主机时的策略，自动添加策略，保存服务器的主机名和密钥信息。
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname=ipaddr, port=port, username=user, password=passwd, timeout=4, allow_agent=False)
    return ssh


# 执行命令，返回结果
def execute_command(ssh_object, command_line):
    # 执行命令
    stdin, stdout, stderr = ssh_object.exec_command(command_line)
    # 获取命令结果
    res_out = stdout.read()
    # 输出命令结果
    print(res_out)


# 关闭连接
def disconnect(ssh_object):
    ssh_object.close()


# 检查是否为危险命令，执行并返回执行结果
def command_check_execute(ssh_objcet, command_line):
    command_list = ['reboot', 'shutdown', 'kill', 'rm', 'restart']
    if command_line in command_list:
        print("危险命令,不允许执行！！")
    else:
        print("你输入的命令是：", command_line)
        execute_command(ssh_objcet, command_line)


# 执行程序
def run(passwd, ipaddr, hostname):
    if isinstance(passwd, list):
        ssh = []
        for i in range(len(passwd)):
            ssh.append(ssh_connect(passwd[i], ipaddr[i]))
        while True:
            command_line = input("请输入命令,退出请输入exit：")
            if command_line == 'exit':
                # 列表推导，关闭所有对象
                [disconnect(each_ssh) for each_ssh in ssh]
                break
            else:
                # 列表推导，执行每个对象的命令
                [command_check_execute(each_ssh, command_line) for each_ssh in ssh]
    elif isinstance(passwd, str):
        ssh = ssh_connect(passwd, ipaddr)
        while True:
            command_line = input("请输入命令,退出请输入exit：")
            if command_line == 'exit':
                disconnect(ssh)
                exit(0)
            else:
                command_check_execute(ssh, command_line)


# 检查参数是否正确，并开始执行命令
def args_check_run(args):
    parser_obj = init_parser()
    if len(args) != 3 and len(args) != 5:
        parser_obj.print_help()
    elif len(sys.argv) == 5:
        (options, args) = parser_obj.parse_args()
        ipaddr, passwd, hostname = read_config(options.nodetype, options.hostname)
        run(passwd, ipaddr, hostname)
    # 参数长度为3
    else:
        (options, args) = parser_obj.parse_args()
        ipaddr, passwd, hostname = read_config(options.hostname)
        run(passwd, ipaddr, hostname)


if __name__ == '__main__':
    args_check_run(sys.argv)
































    # if len(sys.argv) != 3 and len(sys.argv) != 5:
    #     optpar.print_help()
    # elif len(sys.argv) == 5:
    #     (options, args) = optpar.parse_args()
    #     cipaddr, cpasswd = read_config(options.nodetype, options.hostname)
    #     ssh = ssh_connect(cpasswd, cipaddr)
    #     while True:
    #         command_line = input("请输入命令,退出请输入exit：")
    #         if command_line == 'exit':
    #             disconnect(ssh)
    #             exit(0)
    #         else:
    #             command_check_execute(ssh, command_line)
    # elif len(sys.argv) == 3:
    #     (options, args) = optpar.parse_args()
    #     cipaddr, cpasswd = read_config(options.hostname)
    #     ssh = ssh_connect(cpasswd, cipaddr)
    #     while True:
    #         command_line = input("请输入命令,退出请输入exit：")
    #         if command_line == 'exit':
    #             disconnect(ssh)
    #             exit(0)
    #         else:
    #             command_check_execute(ssh, command_line)
    # else:
    #     exit(0)







