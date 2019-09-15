#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/14 17:25
@File    : No182 Duplicate Emails
@Software: PyCharm
"""
select Email from Person group by Email having count(Email) > 1;