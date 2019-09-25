#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/23 18:01
@File    : mafengwo2020_kaoshi
@Software: PyCharm
"""
# def compare(a, b):
#     if a[0] > b[0]: return True
#     elif a[0] == b[0]:
#         if a[1] < b[1]:
#             return True
#         else:
#             return False
#     else:
#         return False
# if __name__ == '__main__':
#     info = input().split(" ")
#     info = set(info)
#     d = {}
#     for i in info:
#         id, place = i.split("-")
#         if place in d.keys():
#             d[place][0] += 1
#         else:
#             d[place] = [1, place]
#     temp = []
#     for i in d.keys():
#         temp.append(d[i])
#     for i in range(len(temp)):
#         for j in range(len(temp)-i-1):
#             if not compare(temp[j], temp[j+1]):
#                 temp[j], temp[j+1] = temp[j+1], temp[j]
#     print(temp[0][1], temp[0][0])
#     print(temp[1][1], temp[1][0])
#     print(temp[2][1], temp[2][0])
if __name__ == '__main__':
    nums = list(map(int, input().split(",")))
    n = int(input())
    if n * 2 + 1 <= max(nums):
        while n * 2 + 1 < max(nums):
            n = n * 2 + 1
        print(n)
    elif n % 2 == 0:
        print(int(n / 2))
    else:
        print(n // 2 / 2)


