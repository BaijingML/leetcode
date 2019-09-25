#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/17 13:51
@File    : danlimoshi
@Software: PyCharm
"""
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance

class A(Singleton):
    pass