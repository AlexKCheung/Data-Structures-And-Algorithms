# 283. Move Zeroes
'''
Given an integer array nums, 
move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # array in place , so we use two pointer method
    current = 0
    zeroes = 0
    for i in range(len(nums)): 
        if nums[i] == 0:
            zeroes += 1
        if nums[i] != 0:
            nums[current] = nums[i] 
            current += 1
    non_zeroes = len(nums) - zeroes
    for i in range(non_zeroes, len(nums)):
        nums[i] = 0
    