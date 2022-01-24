def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force: iterate through array, iterate through rest to find two sum
        # O(n^2) time, O(1) space
        
        # sort nums
        # iterate through array, binary search rest of array to find the two sum
        # O(nlogn) time, O(n) space for .sort()
        
        # iterate through array
        # use hashmap to keep track of integers' passed
        # O(n) time, O(n) space
        
        temp = {}
        
        for i in range(len(nums)): 
            if nums[i] in temp:
                return [temp[nums[i]], i]
            # else
            temp[target-nums[i]] = i
        # assume exactly one solution so nothing to return in end