#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.6
@Author  : Zhangfusheng
@Time    : 2019/9/4 20:14
@File    : 8_sort_algorithm
@Software: PyCharm
"""
"""冒泡排序"""
def bubble(nums):
    """每次从后往前比较，交换两个元素，将最大的排在后面"""
    n = len(nums)
    for i in range(n):
        for j in range(n-1, i, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
    return nums

"""选择排序"""
def select(nums):
    """把最小的元素选择到最前面"""
    n = len(nums)
    m = 0
    for i in range(n):
        m = i
        for j in range(i+1, n):
            if nums[m] > nums[j]:
                m = j
        if i != m:
            nums[i], nums[m] = nums[m], nums[i]
    return nums

def partion(arr, low, high):
    pivotkey = arr[low]
    while low < high:
        while low < high and arr[high] >= pivotkey:
            high -= 1
        arr[high], arr[low] = arr[low], arr[high]
        while low < high and arr[low] <= pivotkey:
            low += 1
        arr[high], arr[low] = arr[low], arr[high]
    return low
def quick_sort(S, low, high):
    if low < high:
        pivot = partion(S, low, high)
        quick_sort(S, low, pivot - 1)
        quick_sort(S, pivot + 1, high)
    return S

if __name__ == "__main__":
    s = [2, 33, 67, 88, 4, 23.4, 9]
    print(bubble(s))
    print(select(s))
    print(quick_sort(s, 0, len(s)-1))