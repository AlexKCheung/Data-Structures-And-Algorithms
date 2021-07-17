#1903. Largest Odd Number in String
'''
You are given a string num, representing a large integer. 
Return the largest-valued odd integer (as a string) that is a non-empty substring of num, 
or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.
'''

def largestOddNumber(self, num: str) -> str:
    # because more digits in spaces increases value by *10
    # we find first occurence of odd digit, scanning from right to left
    place = 0
    for i in range(len(num), 0, -1):
        print(i)
        if int(num[i - 1]) % 2 == 1:
            place = i
            break
    output = num[0:place]
    return output