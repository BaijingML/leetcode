#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2020/1/10 19:58
@File    : No1290 Convert Binary Number in a Linked List to Integer
@Software: PyCharm
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head):
        res = 0
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        for i in range(len(temp) - 1, -1, -1):
            if temp[i] == 1:
                res += 2 ** (len(temp) - 1 - i)
        return res

if __name__ == '__main__':