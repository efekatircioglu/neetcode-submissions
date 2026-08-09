# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove the nth node by changing cur cur.next prev...
        # dummy -> head -> None
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, dummy

        # Advance right by n steps.
        for i in range(n):
            right=right.next
        # Move both left and right forward one step at a time until right reaches the very last node.
        while right and right.next:
            left=left.next
            right=right.next
        # left is now standing before the node to be deleted and right is the node that left should be linked to 
        # Perform the "jump" (re-linking).
        left.next = left.next.next
        # if left == dummy and right.next == None:
        #     left.next = None
        # elif right.next == None and left == dummy:
        #     while left.next.next != right:
        #         left = left.next

        
        # else:
        #     left.next = right
        

        return dummy.next


        # if right.next == None and left == dummy:
        #     while left.next.next != right:
        #         left = left.next

        




        # if right.next == None:
        #     left.next = None
        # else:
        #     left.next=right


    # dummy -> head = [1,2,3,4] -> None
    # , n = 2
    # dummy -> head = [5] -> None , n = 1
    # dummy -> head = [1,2] -> None , n = 2


        