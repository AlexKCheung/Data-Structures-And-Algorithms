# 1991. Find the Middle Index in Array
''' 
Given a 0-indexed integer array nums, 
find the leftmost middleIndex 
(i.e., the smallest amongst all the possible ones).

A middleIndex is an index where 
nums[0] + nums[1] + ... + nums[middleIndex-1] 
== nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. 
Similarly, if middleIndex == nums.length - 1, 
the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, 
or -1 if there is no such index.
''' 

def findMiddleIndex(self, nums: List[int]) -> int:
        # approach: first iterate nums one time to calculate total sum
        # iterate again, this time decreasing sum by current number each time
        # if numbers match: thats the middle position
        # if reach the end and no match: return leftmost index of -1
        total_sum = 0
        for i in nums:
            total_sum += i
        
        current_sum = 0
        
        for i in range(len(nums)):  
            total_sum -= nums[i] 
            if current_sum == total_sum: 
                return i
            current_sum += nums[i]
            
        return -1
        # O(n) runtime for iterating nums twice
        # O(1) space for total_sum and current_sum 