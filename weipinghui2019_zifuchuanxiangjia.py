#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/18 12:04
@File    : weipinghui2019_zifuchuanxiangjia
@Software: PyCharm
"""
if __name__ == "__main__":
    s1, s2 = input(), input()
    result = ""
    add = 0
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    s1, s2 = s1[::-1], s2[::-1]
    for index, i in enumerate(s1):
        if index > len(s2) - 1:
            b = 0
        else:
            b = int(s2[index])
        result += str((int(s1[index]) + b + add) % 2)
        if int(s1[index]) + b + add > 1:
            add = 1
        else:
            add = 0
    if add == 1:
        result += str(1)
    print(result[::-1])


