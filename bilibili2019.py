#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/20 17:29
@File    : bilibili2019
@Software: PyCharm
"""
# temp = sorted(temp, key=lambda x: x[2])
if __name__ == "__main__":
    import sys
    while True:
        try:
            tmp = []
            line = sys.stdin.readline().strip()
            if line == '':
                break
            else:
                tmp.append(line)
            hashTable = {}  # 创建一个哈希表用来将字符映射为一个数字
            for i in range(len(tmp)):
                string = tmp[i]
                for i in range(len(string)):
                    if string[i] == ' ':
                        break
                k = int(string[0:i])
                char = string[i + 1:]
            s = input().split(" ")
            if s:
                N = int(s[0])
                s = "".join(s[1:])
                m = len(s)
                d = {}
                for i in range(m):
                    if s[i] in d.keys():
                        d[s[i]] += 1
                    else:
                        d[s[i]] = 1
                count = 0
                for i in s:
                    if d[i] == 1:
                        count += 1
                    if count == N:
                        print("[" + i + "]")
                        break
                if count < N:
                    print("Myon~")
            else:
                print()
        except:
            break

