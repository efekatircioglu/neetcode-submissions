# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        result = []

        while queue:
            qLen = len(queue)
            level=[]
            for i in range(qLen):
                node=queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                result.append(level)
        
        rightSideView=[]
        for level in result:
            if level:
                rightSideView.append(level[-1])
                

        return rightSideView

                
             