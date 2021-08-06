#125. Valid Palindrome
'''
Given a string s, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.
'''
def isPalindrome(self, s: str) -> bool:
        # ignore spaces and special characters like ,.:
        # first convert into array 
        characters = list()
        count = 0
        for i in s: 
            # only alphanumeric characters
            if i.isalnum(): 
                characters.append(i.lower())
                count += 1
            '''
            a-z and A-Z
            if i.lower() >= 'a' and i.lower() <= 'z': 
                characte    rs.append(i.lower())
                count += 1
            '''
        
        # check if array is a palindrome 
        for i in range(len(characters) // 2): 
            if characters[i] != characters[-(i+1)]: 
                return False

        return True
    # time would be O(n) for linear scan of s
    # space would be O(n) for s