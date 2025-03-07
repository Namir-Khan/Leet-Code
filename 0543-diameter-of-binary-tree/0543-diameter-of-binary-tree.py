# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dMeter = 0

        def depth(root):
            nonlocal dMeter
            if not root:
                return 0

            lDepth = depth(root.left)
            rDepth = depth(root.right)

            dMeter = max(dMeter, lDepth + rDepth)

            return 1 + max(lDepth, rDepth)

        depth(root)
        return dMeter