# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftdepth = self.minDepth(root.left)  
        rightdepth = self.minDepth(root.right)  
        if root.left is None and root.right is None:
            return 1
        if not root.left:
            return 1+rightdepth
        if not root.right:
            return 1+ leftdepth

        return min(leftdepth, rightdepth) +1
  
