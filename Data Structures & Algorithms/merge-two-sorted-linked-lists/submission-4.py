# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # time O(n) space O(1)

        # list1 first, list2 second
        # create an object of the class as dummy
        # tail = dummy
        # while list1 and list2
        # find which value is smaller,

        # then tail=tail.next

        # check edge case when either l1/l2 is empty
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next

        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        
        return dummy.next
