# 237. Delete Node in a Linked List
'''
Write a function to delete a node in a singly-linked list. 
You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next

print("Input with head = [4, 5, 1, 9], node = 5 should output [4, 1, 9]")
print("Input with head [1, 2, 3, 4], node = 3 should outupt [1, 2, 4]")