#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/12 20:40
@File    : 582020_kaoshi
@Software: PyCharm
"""
if __name__ == '__main__':
    info = input().split(",")
    d = {}
    for i in range(len(info)):
        if info[i][-1] == "d" or info[i][-1] == "e":
            if info[i] in d.keys():
                d[info[i]] += 1
            else:
                d[info[i]] = 1
    result = ""
    for i in d.keys():
        result += i + "=" + str(d[i]) + ", "
    print("{"+result[:-2]+"}")
if __name__ == '__main__':
    str1 = input()
    d = {}
    count = 1
    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
            if i != len(str1)-1:
                continue
            else:
                if str1[i] in d.keys():
                    d[str1[i]] += count
                else:
                    d[str1[i]] = count
        else:
            if str1[i-1] in d.keys() and count > 1:
                d[str1[i-1]] += count
            elif count > 1:
                d[str1[i-1]] = count
            count = 1

    s = sorted(d.items(), key=lambda d: d[1], reverse=True)
    for i in range(len(s)):
        print(str(s[i][0])+":"+str(s[i][1]))