#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/19 20:37
@File    : pufa2020_shuzizhuanerjinzhi
@Software: PyCharm
"""
def trans(n):
    result = ""
    while n > 1:
        result += str(n % 2)
        n = int(n / 2)
    result += str(n)
    return result[::-1]
print(trans(13))

def judge(s):
    if not s:
        return False
    else:
        s = s.split(".")
        if 255 >= int(s[0]) > 0:
            if 255 >= int(s[1]) >= 0:
                if 255 >= int(s[2]) >= 0:
                    if 255 >= int(s[3]) >= 0:
                        return True
    return False
print(judge("1.3.11.123"))

def judge_num(s):
    for i in s:
        if 0 <= ord(i) - ord("0") <= 9:
            continue
        else:
            return False
    return True
print(judge_num("123"))

def tranT(nums):
    m = len(nums)
    n = len(nums[0])
    result = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][i] = nums[i][j]
    return result
print(tranT([[1,2,3], [4,5,6]]))


def bubbleSort(arr):
    n = len(arr)
    # for i in range(n):
    #     for j in range(n - i - 1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print(bubbleSort([1,4,2,7]))

def count1(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count
print(count1(5))

def substring(s):
    result = []
    for i in s:
        result.append(i)
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            result.append(s[i:j+1])
    result.remove(s)
    return result
print(substring("abcd"))

def find1(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for i in d.keys():
        if d[i] == 1:
            return i
print(find1("asdfadf"))

def leftadd(s, m, n):
    result = ""
    result += str(m) * n + s
    return result
print(leftadd("123", 0, 9))

def gongbeishu(m, n):
    def gcd(m, n):
        if n > 0:
            return gcd(n, m % n)
        else:
            return m
    return m*n / gcd(m ,n)
print(gongbeishu(8, 4))

