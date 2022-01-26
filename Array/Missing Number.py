# 268 Missing Number
def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        # edge case
        return len(nums)