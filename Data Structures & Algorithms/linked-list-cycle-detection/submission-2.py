# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # l=0,r=1 l+=1  r+=2
        # loop ends when fast becomes null
        # if there's cycle at some point l == r will happen
        l,r= head, head

        while r and r.next:
            # keep iterating until they meet
            l=l.next
            r=r.next.next

            if l==r:
                return True

        return False