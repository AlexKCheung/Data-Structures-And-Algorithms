# 1480. Running Sum of 1d Array
''' 
Given an array nums. 
We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.
'''
# import List for input
from typing import List

def runningSum(nums: List[int]):
    current_sum = 0
    output_list = []
    for i in range(len(nums)): 
        current_sum += nums[i]
        output_list.append(current_sum)
    return output_list

print(runningSum([1, 2, 3, 4]))
print(runningSum([1, 1, 1, 1, 1]))
print(runningSum([3, 1, 2, 10, 1]))
print("Output should be: ")
print("[1, 3, 6, 10]")
print("[1, 2, 3, 4, 5]")
print("[3, 4, 6, 16, 17]")