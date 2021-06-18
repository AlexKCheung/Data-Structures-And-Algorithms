# 136. Single Number
''' 
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
# import List for input
from typing import List

def singleNumber(nums: List[int]) -> int:
    record = {}
    for i in nums:
        record[i] = record.get(i, 0) + 1
    for i in record:
        if record[i] == 1:
            return i

print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1]))
print("\nOutput should be: ")
print("1")
print("4")
print("1")