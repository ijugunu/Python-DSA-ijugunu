# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        height = self.solve(root)
        return height        

    def solve(self,node):
        if node == None:
            return 0
        lh = self.solve(node.left)
        rh = self.solve(node.right)
        return 1 + max(lh,rh)        