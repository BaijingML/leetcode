#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/10/8 18:15
@File    : No137 Single Number II
@Software: PyCharm
"""
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))