# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        # Search Phase
        if key > root.val:
            # go right
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # go left
            root.left = self.deleteNode(root.left, key)
        # Deletion Phase
        else:
            # Case A) node has 0 or 1 child
            if not root.left:
                # if there's no left child, return right child
                return root.right
            elif not root.right:
                # if there's no right child, return left child
                return root.left
            
            # Case B) node has 2 child
            # To delete a node with 2 children, first find a replacement node
            # Find min from right subtree (leftmost child of right subtree) (could have vice versa)
            cur = root.right
            while cur.left:
                # keep going until the minimum node in right subtree
                cur = cur.left
            # Replace the root with replacement value
            root.val = cur.val
            # Delete the original replacement node
            root.right = self.deleteNode(root.right, root.val)
            
        return root 
        