# 1450. Number of Students Doing Homework at a Given Time
'''
Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].
Return the number of students doing their homework at time queryTime. 
More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
'''

# import List for input
from typing import List

def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
        timetable = {}
        for i in range(len(startTime)): 
            for time in range(startTime[i], endTime[i] + 1):
                timetable[time] = timetable.get(time, 0) + 1
        if not queryTime in timetable:
            return 0
        else: 
            return timetable[queryTime]

print(busyStudent([1, 2, 3], [3, 2, 7], 4))
print(busyStudent([4], [4], 4))
print(busyStudent([4], [4], 5))
print(busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7))
print(busyStudent([9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5))
print("\nOutput should be: ")
print("1\n1\n0\n0\n5")