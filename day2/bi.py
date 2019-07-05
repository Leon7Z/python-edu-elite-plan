import sys


def command_check(a):
    '''
    哈哈哈
    :param a:
    :return:
    '''
    command_list = ['reboot', 'shutdown', 'kill', 'rm', 'restart']
    if a in command_list:
        print("危险命令")
    else:
        print("你输入的命令是：", a)


# command = input("请输入命令：")
if len(sys.argv) != 2:
    print("请传一个参数")
else:
    command_check(sys.argv[1])


