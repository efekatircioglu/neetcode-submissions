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
        res=[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur= cur.left
            cur=stack.pop()
            if i<k:
                res.append(cur.val)
                i+=1
            if i==k:
                return res.pop()
            cur=cur.right