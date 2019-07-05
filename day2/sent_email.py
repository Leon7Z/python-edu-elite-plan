import sys, smtplib, configparser, os
from email.mime.text import MIMEText
from email.utils import formataddr


# 读取配置文件
base_dir = r'C:\Users\zxleo\PycharmProjects\python-edu\day2'
path = os.path.join(base_dir, 'config.ini')

conf = configparser.ConfigParser()  # 定义一个对象接收
conf.read(path)

print(type(conf['email']['username']))
print(type(conf['email']['password']))
# my_sender = 'zx-leon@163.com'  # 发件人邮箱账号
# my_pass = 'ada850729'  # 发件人邮箱密码
# my_user = 'zx-leon@163.com'  # 收件人邮箱账号，我这边发送给自己


def mail(emailaddr, title, body):
    ret = True

    try:
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = formataddr(["Leon", conf['email']['username']])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["TT", emailaddr])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL(conf['email']['smtp_server'], 465)  # 发件人邮箱中的SMTP服务器，端口是25
        # print(conf['email']['username'], conf['email']['password'])
        server.login(conf['email']['username'], conf['email']['password'])  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(conf['email']['username'], [emailaddr, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as error:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(error)
        ret = False
    return ret


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("使用方法：3个参数 邮箱地址 主题 内容")
    else:
        result = mail(sys.argv[1], sys.argv[2], sys.argv[3])
        if result:
            print("邮件发送成功")
        else:
            print("邮件发送失败")
