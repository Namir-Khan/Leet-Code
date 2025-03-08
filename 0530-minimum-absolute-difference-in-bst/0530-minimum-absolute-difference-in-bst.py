# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = float('inf')
        prevVal = float('-inf')

        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                minDiff = min(minDiff, root.val - prevVal)
                prevVal = root.val
                root = root.right

        return minDiff