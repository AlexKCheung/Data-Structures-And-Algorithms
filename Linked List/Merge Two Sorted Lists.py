#21. Merge Two Sorted Lists
'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.
'''

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = output = ListNode(0)
        while l1 and l2: 
            if l1.val < l2.val: 
                output.next = l1
                l1 = l1.next
            else: 
                output.next = l2
                l2 = l2.next
            output = output.next
        output.next = l1 or l2
        return temp.next