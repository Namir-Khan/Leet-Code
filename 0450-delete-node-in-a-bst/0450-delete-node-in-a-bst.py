# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        parent = None # Prev node
        curr = root

        # Find the node to delete and its prev node i.e parent
        while curr and curr.val != key:
            parent = curr
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # Node not found
        if not curr:
            return root

        # Case 1: Node with no child node
        if not curr.left and not curr.right:
            if not parent:
                return None
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node with 1 child node
        elif not curr.left or not curr.right:
            child =  curr.left if curr.left else curr.right
            if not parent:
                return child
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Case 3: Node with 2 child node
        else:
            # Inorder smallest term in right sub tree
            succesorParent = curr
            succesor = curr.right
            while succesor.left:
                succesorParent = succesor
                succesor = succesor.left

            curr.val = succesor.val

            if succesorParent.left == succesor:
                succesorParent.left = succesor.right
            else:
                succesorParent.right = succesor.right

        return root