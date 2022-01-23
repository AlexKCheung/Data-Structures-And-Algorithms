def containsDuplicate(self, nums: List[int]) -> bool:
        # brute force: loop through array, iterate rest to see if appears twice
        # O(n^2) time, O(1) space
        
        # use dictionary to keep track of met values
        # if value in dictionary already exists, return false
        # if reach end of array and no duplicated, return true
        # O(n) time, O(n) space
        '''
        meetValues = {}
        for i in nums:
            if i in meetValues:
                return True
            meetValues[i] = True
        return False
        '''
        
        
        # sort array, then iterate checking if next value is equal to current value
        # O(nlogn) time, O(n) space depending on sort
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False
        
        # python set properties
        # return len(nums) != len(set(nums))