# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do a inorder traversal
        i=0
        cur=root
        stack=[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur= cur.left
            cur=stack.pop()    
            i+=1
            if i==k:
                return cur.val
            cur=cur.right