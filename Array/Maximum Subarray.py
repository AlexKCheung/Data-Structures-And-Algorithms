#53. Maximum Subarray
'''
Given an integer array nums, 
find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.
'''
def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        current = 0
        for i in range(len(nums)): 
            current += nums[i]
            if current > maximum: 
                maximum = current
            if current < 0: 
                current = 0

        return maximum