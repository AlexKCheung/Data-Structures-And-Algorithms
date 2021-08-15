#448. Find All Numbers Disappeared in an Array
'''
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
'''
def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    # iterate over nums adding number to data structure
    # data structure can be dictionary[number], iterate check if number in dictionary
    # or can be array with array location represent the numberwith a 0/1 
    
    storage = [0] * len(nums)
    storage.append(0)
    for i in nums: 
        storage[i] = 1
    storage[0] = 1
    output = []
    for i in range(len(storage)): 
        if storage[i] == 0: 
            output.append(i)
    return output