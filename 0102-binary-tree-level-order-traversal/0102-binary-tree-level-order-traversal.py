# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res=[]
        if root is None:
            return res
        
        queue=deque([])
        queue.append(root)

        while queue:
            level_size=len(queue)
            level=[]

            for i in range(level_size):
                curr=queue.popleft()
                level.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)

            res.append(level)           

        return res             