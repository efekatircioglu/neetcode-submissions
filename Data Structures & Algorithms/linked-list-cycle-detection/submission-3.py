# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur=head



        while head:
            if cur in seen:
                return True

            seen.add(cur)
            cur=cur.next
            head=head.next                
    
        return False


        # seen = ()
        # cur=1
        # head= 1,2

        # first iteration:
        # seen = (1)





        