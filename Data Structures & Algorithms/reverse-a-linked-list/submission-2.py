# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]): 
        previous = None
        current = head

        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous