from typing import List
from numpy.random import permutation
'''
归并排序 (Merge)
平均复杂度: O(nlogn)
最坏复杂度: O(n2)
最好复杂度: O(n)

空间复杂度: 1
稳定性: 不稳定

思路: 


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
    def mergeSort(self,arr:List[int],left:int=0,right:int=len(arr)-1):
        pass

    def merge(self,arr: List[int],leftPtr:int,rightPtr:int,rightBound:int)-> List[int]: #治-排序
        Start = leftPtr
        if leftPtr == rightPtr:
            return 
        leftBound = rightPtr-1
        temp = []
        while leftPtr<=leftBound and rightPtr <= rightBound:
            if arr[leftPtr] < arr[rightPtr]:
                temp.append(arr[leftPtr])
                leftPtr+=1
            else:
                temp.append(arr[rightPtr])
                rightPtr+=1 
        while(leftPtr<=leftBound):
            temp.append(arr[leftPtr])
            leftPtr+=1 
        while(rightPtr<=rightBound):
            temp.append(arr[rightPtr])
            rightPtr+=1 
        arr[Start:rightBound+1] = temp

arr = [1,3,6,2,7,8,5,6,9]
print(arr)
Solution().merge(arr,3,6,len(arr)-1)
print(arr) 