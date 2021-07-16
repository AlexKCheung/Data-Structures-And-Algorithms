#1919. Concatenation of Array
'''
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] 
and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
'''

def getConcatenation(self, nums: List[int]) -> List[int]:
    output_list = []
    for times in range(2):
        for i in nums:
            output_list.append(i)
    return output_list