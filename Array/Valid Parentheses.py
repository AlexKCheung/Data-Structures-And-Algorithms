
def isValid(self, s: str) -> bool:
    
    parentheses = {'(':')', '{':'}', '[':']'}
    
    stack = []
    
    for i in s:
        if i in parentheses:
            stack.append(i)
        elif len(stack) == 0 or parentheses[stack.pop()] != i:
            return False
        
    if len(stack) == 0:
        return True
    return False
    
    # O(n) runtime
    # O(n) memory 
