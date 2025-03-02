# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find middle
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now reverse
        prevP = None
        while slow:
            nextP = slow.next
            slow.next = prevP

            prevP = slow
            slow = nextP

        # Check with new pointers check palindrome
        left = head
        right = prevP

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next
            
        return True