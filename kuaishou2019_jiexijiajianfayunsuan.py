#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/27 22:01
@File    : kuaishou2019_jiexijiajianfayunsuan
@Software: PyCharm
"""
if __name__ == "__main__":
    result = 0
    str1 = input()
    str1 = "0" + str1
    s = str1.split("+")
    for i in s:
        if "-" in i:
            t = [int(j) for j in i.split("-")]
            result += t[0] - sum(t[1:])
        else:
            result += int(i)
    print(result)

