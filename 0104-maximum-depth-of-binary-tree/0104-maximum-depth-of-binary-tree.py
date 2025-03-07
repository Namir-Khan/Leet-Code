# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])

        while queue:
            node, lev = queue.popleft()

            if node.left:
                queue.append((node.left, lev + 1))
            if node.right:
                queue.append((node.right, lev + 1))

        return lev