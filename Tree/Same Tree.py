#100. Same Tree
'''
Given the roots of two binary trees p and q, 
write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
'''

def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # iterate through both trees at the same time
    # if found any difference then return false
    # else return true 
    
    # recursion
    if not p and not q: 
        return True
    if not p or not q: 
        return False
    if p.val != q.val: 
        return False
    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
        