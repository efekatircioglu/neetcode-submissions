# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> null
        # 4 -> 3 -> 2 -> 1 -> null 

        # besides tail, reverse it, then put the tail -> null
        # cur

        # cur, next
        # next=cur
        prev, cur= None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


        