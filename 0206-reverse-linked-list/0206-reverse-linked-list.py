# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevP = None
        currP = nextP = head

        while currP:
            nextP = currP.next
            currP.next = prevP

            prevP = currP
            currP = nextP

        head = prevP

        return head