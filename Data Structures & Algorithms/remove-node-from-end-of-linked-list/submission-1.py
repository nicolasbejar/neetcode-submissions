# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # Reverse
        prev = None
        current = head
        while current:
            nextOne = current.next
            current.next = prev
            prev = current 
            current = nextOne 

        newHead = prev

        prev = None
        current = newHead
        # Remove
        while current:
            n -= 1
            if n == 0:
                nextOne = current.next
                if prev:
                    prev.next = nextOne
                else:
                    newHead = nextOne
                current = nextOne
                break

            prev = current 
            current = current.next
            

        # Reverse again
        prev = None
        current = newHead
        while current:
            nextOne = current.next
            current.next = prev
            prev = current 
            current = nextOne 

        return prev

        
        