#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/30 21:29
@File    : zhaoshang2019_tiaoxuandaibiao
@Software: PyCharm
"""
def call(n, info):
    temp = [info[0][0], info[0][1]]
    for i in range(1, n):
        if info[i][0] > temp[-1]:
            temp.append(info[i][0])
            temp.append(info[i][1])
        elif info[i][0] == temp[-1]:
            temp.append(info[i][1])
    return len(temp)
if __name__ == "__main__":
    n = int(input())
    info = []
    if n > 1:
        for i in range(n):
            info.append(list(map(int, input().split(" "))))
        info.sort(key=lambda x:x[1])
        print(call(n, info))
    else:
        print(n * 2)