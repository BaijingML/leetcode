#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/8/28 20:49
@File    : binary_search
@Software: PyCharm
"""
def binary_search(list_item, item):
    low = 0
    high = len(list_item)
    while low < high:
        mid = int((low + high) / 2)
        guess = list_item[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid
        else:
            low = mid + 1
    return None

if __name__ == "__main__":
    list_item = [1, 3, 5, 7, 9, 23, 43, 57, 58, 60, 76, 89, 100]
    index = binary_search(list_item, 89)
    print('查找的索引是{0}，对应的数字是{1}'.format(index, list_item[index]))
