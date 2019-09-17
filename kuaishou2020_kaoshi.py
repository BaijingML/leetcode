#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/16 21:02
@File    : kuaishou2020_kaoshi
@Software: PyCharm
"""
# if __name__ == '__main__':
#     x_min, y_min, x_max, y_max = float("inf"), float("inf"), -float("inf"), -float("inf")
#     info = input().split(",")
#     for i in info:
#         x, y = i.split(" ")
#         x, y = int(x), int(y)
#         if x < x_min:
#             x_min = x
#         if x > x_max:
#             x_max = x
#         if y > y_max:
#             y_max = y
#         if y < y_min:
#             y_min = y
#     result = []
#     result.append(str(x_min) + " " + str(y_min))
#     result.append(str(x_min) + " " + str(y_max))
#     result.append(str(x_max) + " " + str(y_max))
#     result.append(str(x_max) + " " + str(y_min))
#
#     for i in range(len(result)):
#         if i == len(result) - 1:
#             print(result[i])
#         else:
#             print(result[i], end = ",")

# if __name__ == '__main__':
#     nums = list(map(int, input().split(",")))
#     count = 0
#     for i in range(1, len(nums)-1):
#         if nums[i] > nums[i-1]:
#             continue
#         count += 1
#         if i-2 >= 0 and nums[i-2] > nums[i]:
#             nums[i] = nums[i-1]
#     if count > 1:
#         print(0)
#     else:
#         print(1)
# def call(mylist):
#     n = len(mylist)
#     left, maxl = 0, 0
#     for i in range(n):
#         if i - maxl >= 1 and mylist[i-maxl:i+1] == mylist[i-maxl:i+1][::-1]:
#             left = i - maxl - 1
#             maxl += 2
#         if i - maxl >= 0 and mylist[i- maxl:i+1] == mylist[i- maxl:i+1][::-1]:
#             left = i - maxl
#             maxl += 1
#     return mylist[left:left + maxl]
# def call(mylist):
#     n = len(mylist)
#     temp = [[0 for _ in range(n)] for _ in range(n)]
#     result = ""
#     maxl = 0
#     for i in range(n):
#         for j in range(i+1):
#             if mylist[j] == mylist[i]:
#                 temp[j][i] = 1
#                 if maxl < i - j + 1:
#                     maxl = i - j + 1
#                     result = mylist[j:i+1]
#             else:
#                 if mylist[j] == mylist[i] and temp[j+1][i-1]:
#                     temp[j][i] = 1
#                     if maxl < i - j + 1:
#                         result = mylist[j:i+1]
#                         maxl = i - j + 1
#     return result
#
# if __name__ == '__main__':
#     str1 = input()
#     mylist = list(str1)
#     print("".join(call(mylist)))
def convert(s, n):
    result = [""] * min(len(s), n)
    currentrow = 0
    topdown = False
    for i in s:
        result[currentrow] += i
        if currentrow == 0 or currentrow == n-1:
            topdown = not topdown
            if topdown:
                currentrow += 1
            else:
                currentrow -= 1
    return "".join(result)
if __name__ == '__main__':
    str1, n = input().split(",")
    n = int(n)
    if n == 1:
        print(str1)
    else:
        print(convert(str1, n))
