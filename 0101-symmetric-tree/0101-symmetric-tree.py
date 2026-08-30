# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(leftTree: Optional[TreeNode], rightTree: Optional[TreeNode]) -> bool:
            if not leftTree and not rightTree:
                return True
            if leftTree and not rightTree or rightTree and not leftTree or leftTree.val != rightTree.val:
                return False
            return isMirror(leftTree.left, rightTree.right) and isMirror(leftTree.right, rightTree.left)

        return isMirror(root.left, root.right)
