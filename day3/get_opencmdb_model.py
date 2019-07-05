#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 17:39
# @Author  : Leon Zhou
# @Email   : hbzhoux@189.cn
# @File    : get_opencmdb_model.py
# @Software: PyCharm
import requests


def get_token():
    payload = "{ \"email\": \"admin@opencmdb.cn\", \"password\": \"opencmdb\"}"
    # payload = {"email": "admin@opencmdb.cn", "password": "opencmdb"}

    headers = {"accept": "application/json", "Content-Type": "application/json"}
    # r = requests.get("http://www.opencmdb.cn/api/v0.1/login", params=payload)
    r = requests.post("http://www.opencmdb.cn/api/v0.1/login", data=payload, headers=headers)
    print(r.json())
    return r.json()['authentication_token']


def get_models(token):
    # headers = {"Authentication-Token": token}
    headers = {"Authentication-Token": token}
    r = requests.get("http://www.opencmdb.cn/api/v0.1/moulds", headers=headers)
    print(r.json())


if __name__ == '__main__':
    token = get_token()
    get_models(token)
