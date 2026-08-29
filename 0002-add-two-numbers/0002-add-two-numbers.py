# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        c = 0 #carry


        while (l1 is not None or l2 is not None or c != 0):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            digit = (val1 + val2 + c) % 10
            if (val1 + val2 + c >= 10):
                c = 1
            else:
                c = 0

            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
            

        