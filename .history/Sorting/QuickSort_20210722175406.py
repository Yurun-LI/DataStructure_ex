from typing import List
from numpy.random import permutation
'''
快速排序 (Quick))
平均复杂度: O(nlogn)
最坏复杂度: O(nlogn)
最好复杂度: O(nlogn)

空间复杂度: n
稳定性: 稳定

思路: 
采用分而治之的方法
将数组先分,而后在重新合并

伪代码:
def sort():
    mid = left + (right-left) // 2
    sort(arr[left:mid])
    sort(arr[mid+1:right])
    merge(arr)->合并左右侧的两个有序数组

用途:速度仅次于快速排序，为稳定排序算法，一般用于对总体无序，但是各子项相对有序的数列
'''
# time
import time
from functools import wraps


def timeCount(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}的运行时间为{end-start}')
        return result
    return wrapper


class Solution:
    def quickSort(self, arr: List[int]):
        def sort(arr, leftBound, rightBound):
            if leftBound >= rightBound:
                return
            mid = leftBound + (rightBound-leftBound) >> 1
            sort(arr, leftBound, mid)
            sort(mid+1, rightBound)
            partition()

    def partition(self, arr: List[int], leftBound: int, rightBound: int):
        if leftBound >= rightBound:
            return
        pivot = arr[rightBound]
        low, high = leftBound, rightBound-1
        # while low<high:
        #     if arr[low] >= pivot:
        #         if arr[high]<=pivot:
        #             arr[low],arr[high] = arr[high],arr[low]
        #             continue
        #         high-=1
        #         continue
        #     low+=1
        while low<high:
            while low<=high and arr[low]<=pivot:
                low+=1 
            while low<=high and arr[high] > pivot:
                high-=1 
            arr[low],arr[high] = arr[high],arr[low]
        arr[high],arr[rightBound] = arr[rightBound],arr[high]
arr = [1, 4, 5, 8, 2, 5, 7, 9, 12, 6, 3]
Solution().partition(arr, 0, len(arr)-1)
print(arr)
