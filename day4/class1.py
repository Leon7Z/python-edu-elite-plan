#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/4 9:45
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : class1.py
# @Software: PyCharm
#
#
# class Person:
#     hh = "222"
#     def __init__(self, name, age):
#         self.hh = name
#         self.aa = age
#
#
#     def say_hi(self):
#         print("111", self.hh, self.aa)
#
#
# class Man(Person):
#     a = 2
#     c = 2
#
# p = Person('leon', 35)
# p.say_hi()


class A:
    count = 0


# sub class do things
class B(A):
    def __init__(self):
        A.count += 1
        self.count = 10



# 测试代码：
if __name__ == '__main__':
    a = B()
    b = B()
    print('B instance count: ', a.count)
    print('B instance count: ', b.count)
    print(A.count)

