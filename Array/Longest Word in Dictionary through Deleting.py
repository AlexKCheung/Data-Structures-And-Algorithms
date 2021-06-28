# 524. Longest Word in Dictionary through Deleting
'''
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. 
If there is more than one possible result, return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.
'''
# modified problem for longest string in the dictionary that can be formed by deleting and reordering some of the given string characters

# import List for input
from typing import List

def findLongestWord(s: str, dictionary: List[str]) -> str:
    available_letters = {}
    # count of each letter occurence in dictionary
    for i in s:
        available_letters[i] = available_letters.get(i, 0) + 1
    
    longest_word = ""
    longest_length = 0
    
    for word in dictionary: 
        temp_word = {}
        # create mini dictionary for each word
        for char in word:
            temp_word[char] = temp_word.get(char, 0) + 1
        for letter in temp_word:
            # if not enough letters for the word word
            if available_letters.get(letter, 0) < temp_word[letter]:
                skip = 1
                break
            else:
                skip = 0
        if skip == 1:
            continue
        # not break yet so enough words
        # bigger word
        if len(word) > longest_length:
            longest_word = word
            longest_length = len(word)
        # same length so longest with smallest lexicographical order
        elif len(word) == longest_length: 
            for i in range(len(word)): 
                if word[i] == longest_word[i]:
                    continue
                elif word[i] < longest_word[i]:
                    longest_word = word
                    break
                else:
                    # else longest word stays the same
                    break
    return longest_word

print(findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(findLongestWord("abpcplea", ["a", "b", "c"]))
print("\nOutput should be:")
print("apple\na")