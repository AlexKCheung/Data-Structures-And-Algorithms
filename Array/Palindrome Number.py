#9. Palindrome Number
'''
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is palindrome while 123 is not.
'''

def isPalindrome(self, x: int) -> bool:
    # base case negative numbers
    if x < 0:
        return False
    
    # else x is > 0
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] == x[-i - 1]:
            continue
        else:
            return False
    return True
    
    