#1941. Check if All Characters Have Equal Number of Occurrences
'''
Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences 
(i.e., the same frequency).
'''

def areOccurrencesEqual(self, s: str) -> bool:
    # iterate s and increment data structure by 1
    # iterate  ata structure and check if it appears equally
    # DS first thought of dictionary 
    # but can use array[26] as s is lowercase English letters
    # but will need to use special function to turn into ascii - 70 something
    # O(n) time complexity for iterating s and DS
    # O(c) space complexity
    alphabet = [0] * 26
    temp = 0
    for i in s: 
        # ascii convert and to 0 index
        temp = ord(i) - 97
        alphabet[temp] += 1
    check = alphabet[temp]
    for i in alphabet: 
        if not i == check and not i == 0: 
            return False
    return True