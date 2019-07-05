# shoplist = ['apple', 'banana', 'mango']
# print('我需要买', len(shoplist), '种水果')
# print('他们分别是：', end='')
# for i in shoplist:
#     print(i, end=' ')
# print('\n我还需要买米饭')
# shoplist.append('rice')
# print('现在的购物列表是', shoplist)
# print('我需要整理下我的购物列表')
# shoplist.sort()
#
#
# del shoplist[0]
command_list = ['reboot', 'shutdown', 'kill', 'rm', 'restart']
i = 0
while i != 5:
    i += 1
    input_command = input('请输入命令：')
    if input_command in command_list:
        print('请注意，不要执行危险命令')
    else:
        print('您输入的命令是：', input_command)
