#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/18 11:40
@File    : kuaishou2019_zifuchuanguiyihua
@Software: PyCharm
"""
if __name__ == "__main__":
    from collections import OrderedDict
    s = input()
    d = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0,
         "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
    d =  OrderedDict(sorted(d.items(),key = lambda t:t[0]))

    for i in s:
        d[i] += 1
    result = ""
    for i in d.keys():
        if d[i] > 0:
            result += i + str(d[i])
    print(result)