# 1. Two Sum
''' 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
# import List for input
from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # brute force very inefficient
    '''
    for i in range(len(nums)): 
        for current in range(i + 1, len(nums)):
            if nums[i] + nums[current] == target:
                return [i, current]
    '''
    # time complexity of O(n), much more efficient
    