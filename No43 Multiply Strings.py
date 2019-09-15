#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/14 19:23
@File    : No43 Multiply Strings
@Software: PyCharm
"""


def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0": return "0"
    result = [0 for _ in range(len(num1) + len(num2))]
    num1 = num1[::-1]
    num2 = num2[::-1]
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += int(num1[i]) * int(num2[j])
    for i in range(len(result)):
        if result[i] >= 10:
            result[i + 1] += result[i] // 10
            result[i] = result[i] % 10

    result = list(map(str, (i for i in result)))
    print(result)
    if result[-1] == "0":
        result = result[:-1]
    return "".join(result[::-1])
if __name__ == '__main__':
    print(multiply("16", "3"))