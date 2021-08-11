#387. First Unique Character in a String
'''
Given a string s, find the first non-repeating character in it 
and return its index. If it does not exist, return -1.
'''
def firstUniqChar(self, s: str) -> int:
    # finding first non repeating character's index
    # can be possible that there are more than one instance of non repeating characters
    # time complexity of O(n) for iterating s twice
    # space complexity of O(n) for storing s in characters
    characters = {}
    for i in range(len(s)): 
        if s[i] not in characters: 
            characters[s[i]] = 1
        else: 
            characters[s[i]] += 1

    for i in range(len(s)): 
        if characters[s[i]] == 1: 
            return i
    
    return -1