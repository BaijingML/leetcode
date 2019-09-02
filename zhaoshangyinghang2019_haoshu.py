#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/29 16:11
@File    : zhaoshangyinghang2019_haoshu
@Software: PyCharm
"""
def call(m):
    temp = ""
    d = {"2":"5", "5":"2", "6":"9", "9":"6", "1":"1", "8":"8", "0":"0"}
    m_str = str(m)
    for i in m_str:
        if i == "3" or i == "4" or i == "7":
            return False
        else:
            temp += d[i]
    if temp == m_str:
        return False
    else:
        return True
if __name__ == "__main__":
    n = int(input())
    count = 0
    for i in range(n+1):
        if call(i):
            count += 1
        else:
            continue
    print(count)