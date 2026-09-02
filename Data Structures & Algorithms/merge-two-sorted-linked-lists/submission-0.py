class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy

        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val < current2.val:
                curr.next = current1
                current1 = current1.next
            else:
                curr.next = current2
                current2 = current2.next

            curr = curr.next

        if current1:
            curr.next = current1

        if current2:
            curr.next = current2

        return dummy.next