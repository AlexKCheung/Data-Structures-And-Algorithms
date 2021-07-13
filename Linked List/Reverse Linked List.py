# 206 Reverse Linked List
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

def reverseList(self, head: ListNode) -> ListNode:
    # iterate through linked list 
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev

