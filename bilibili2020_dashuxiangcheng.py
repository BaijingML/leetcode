#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/20 21:34
@File    : bilibili2020_dashuxiangcheng
@Software: PyCharm
"""
if __name__ == "__main__":
    while True:
        N = input()
        M = input()
        result = ""
        if N == "0" or M == "0":
            result = "0"
        else:

            s = 0
            m, n = len(M), len(N)
            temp = [[] for i in range(m)]
            for i in range(m-1, -1, -1):
                for j in range(n-1, -1, -1):
                    temp[i].append((int(M[i]) * int(N[j]) + s) % 10)
                    s = int(int(M[i]) * int(N[j]) / 10)
                    if j == 0 and s > 0:
                        temp[i].append(s)
                        # temp[i] = temp[i][::-1]
            print(temp)
            if m > 1:
                result += str(temp[0][0])
                add = 0
                for i in range(1, m):
                    for j in range(min(len(temp[i]), len(i-1))):
                        add += temp[j][i]
                    result += str(add % 10)
                    add = int(add / 10)
                if add > 0:
                    result += str(add )
            else:
                for i in range(len(temp[0])):
                    temp[0][i] = str(temp[0][i])
                result = ''.join(temp[0])
            print(result[::-1])