# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next
        # STEP 1) find middle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # loop ended, slow-> middle fast-> tail 
        # STEP 2) make the second part of the list reversed
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # STEP 3) merge these 2 parts on their order
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second=tmp1, tmp2