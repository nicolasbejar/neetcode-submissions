# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        sortedL = []

        for l in lists:
            while l:
                sortedL.append(l.val)
                l = l.next


        sortedL.sort()

        ans = ListNode(0)
        current = ans
        for node in sortedL:
            current.next = ListNode(node)
            current = current.next
        
        return ans.next


        