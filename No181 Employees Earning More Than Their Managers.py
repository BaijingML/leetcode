#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/14 17:33
@File    : Np181 Employees Earning More Than Their Managers
@Software: PyCharm
"""
select Name as Employee from Employee emn where Salary > (select Salary from Employee where Id=emn.ManagerId);
select t0.Name as Employee from Employee t0 join Employee t1 on t0.ManagerId=t1.Id and t0.Salary > t1.Salary;