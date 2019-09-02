#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/27 19:27
@File    : wangyi2019_miludeniuniu
@Software: PyCharm
"""
if __name__ == "__main__":
    N = int(input())
    temp = input()
    count = 0
    for i in temp:
        if i == "L":
            count += 1
        else:
            count -= 1
    if count % 4 == 0:
        print("N")
    elif count % 4 == 1:
        print("W")
    elif count % 4 == 2:
        print("S")
    else:
        print("E")