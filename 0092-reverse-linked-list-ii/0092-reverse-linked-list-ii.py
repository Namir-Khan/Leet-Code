# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)
        currP, prevLeft = head, dummyHead

        for i in range(left-1):
            prevLeft, currP = currP, currP.next

        prevP = None
        for i in range(right - left + 1):
            nextP = currP.next
            currP.next = prevP
            prevP, currP = currP, nextP

        prevLeft.next.next = currP
        prevLeft.next = prevP

        return dummyHead.next