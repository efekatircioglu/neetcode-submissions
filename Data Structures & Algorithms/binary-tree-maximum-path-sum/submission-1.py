# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            # recursively calculate max path sum for left and right children
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)


            leftMax = max(leftMax,0)
            rightMax = max(rightMax, 0)

            #case 1: split at cur node (left + root + right)
            # this cannot be extended to parent but it might be global max
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # case 2: return to parent, pick only one side left/right
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
        