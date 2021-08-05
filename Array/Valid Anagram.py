# 242. Valid Anagram 
'''
Given two strings s and t, 
return true if t is an anagram of s, and false otherwise.
'''
  def isAnagram(self, s: str, t: str) -> bool:
        
        # method one: sort both s and t
        # check if the sorted are the same
        # time: O(nlogn) for built in function sort
        # return sorted(s) == sorted(t)
        
        # method two: iterate through s and t
        # generate dictionaries for each letter occurence
        # compare if the two dictionaries are the same
        # time: O(n) iterate entire s and t
        # space: O(n) 
        # note: can also use python get() function for dictionary 
        s_dict = {}
        t_dict = {}
        for i in s: 
            if i in s_dict:
                s_dict[i] += 1
            else: 
                s_dict[i] = 1
        for i in t: 
            if i in t_dict: 
                t_dict[i] += 1
            else: 
                t_dict[i] = 1
        return s_dict == t_dict
