# 1672. Richest Customer Wealth
''' 
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
'''
# import List for input
from typing import List

def maximumWealth(accounts: List[List[int]]) -> int:
    wealth = 0
    for account in accounts:
        temp = 0
        for value in account:
            temp += value
        if temp > wealth:
            wealth = temp
    return wealth

print(maximumWealth([[1, 2, 3], [3, 2, 1]]))
print(maximumWealth([[1, 5], [7, 3], [3, 5]]))
print(maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
print("\nOutput should be:")
print("6\n10\n17")