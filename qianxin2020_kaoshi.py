#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/9 18:48
@File    : qianxin2020_kaoshi
@Software: PyCharm
"""
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


# def max_length_substring(s):
#     subset = set(s[0])
#     maxl = 1
#     left = 0
#     flag = True
#     for i in range(1, len(s)):
#         if s[i] in subset:
#             maxl = max(maxl, i - left)
#             left = i
#             subset = set(s[i])
#             flag = False
#         else:
#             subset.add(s[i])
#     if flag:
#         return len(s)
#     return maxl
#
#
# # ******************************结束写代码******************************
#
#
# try:
#     _s = input()
# except:
#     _s = None
#
# res = max_length_substring(_s)
#
# print(str(res) + "\n")
if __name__ == '__main__':
    N = int(input())
    m = 5
    members = [i+1 for i in range(N)]
    luck = 0
    bt = 0
    if N == 1:
        print(1)
    else:
        while len(members) > 1:
            bt = (bt+4) % len(members)
            luck += 1
            if members[bt] == N:
                print(luck)
                break
            members.pop(bt)
        if len(members) == 1:
            print(members.pop())
