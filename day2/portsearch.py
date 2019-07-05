import sys
protocal_list = {'ssh': 22, 'http': 80, 'https': 443, 'smtp': 25, 'ftp': 21}


def search_port(protocal):
    # if protocal in protocal_list.keys():
    if protocal in protocal_list:
        print('您查询的协议端口为：', protocal_list.get(protocal))
    else:
        print('对不起，你查询的协议不在库内！')


if len(sys.argv) != 2:
    print("请传一个参数")
else:
    search_port(sys.argv[1])






