# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        n = len(nums)
        mid = n //2
        root = TreeNode(nums[mid])

        # Queue for (parent, left, right)
        queue = deque()
        queue.append((root, 0, mid - 1)) # In eg1 (root, 0, 1) i.e [-10, -3]
        queue.append((root, mid + 1, n - 1)) # In eg2 (root, 3, 4) [5, 9]

        while queue:
            parent, left, right = queue.popleft()
            if left <= right:
                mid = (left + right) // 2
                child = TreeNode(nums[mid])
                if nums[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child
                
                queue.append((child, left, mid - 1))
                queue.append((child, mid + 1, right))

        return root