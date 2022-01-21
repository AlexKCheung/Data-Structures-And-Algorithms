def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    # sort pairs by second element
    boxTypes.sort(key=lambda x:x[1])
    boxTypes = boxTypes[::-1]
    
    units = 0
    
    for i in boxTypes:
        while i[0] > 0 and truckSize > 0:
            units += i[1]
            i[0] -= 1
            truckSize -= 1
    return units