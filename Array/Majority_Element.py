# 169. Majority Element
'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
'''
# import List for input
from typing import List

def majorityElement(nums: List[int]) -> int:
    # iterative solution
    values = {}
    for i in nums: 
        values[i] = values.get(i, 0) + 1
    for i in values:
        if values[i] > len(nums) / 2: 
            return i
        
print(majorityElement([3, 2, 3]))
print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
print("\nOutput should be:")
print("3\n2")