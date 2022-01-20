#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            count += 1
    return count
    
    
    
print(alternatingCharacters('BBBBB')) # expected: 4
print(alternatingCharacters('ABABABAB')) # expected: 0