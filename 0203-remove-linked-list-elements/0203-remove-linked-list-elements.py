# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        dummy_head.next = head
        currP = dummy_head

        while currP.next != None:
            if currP.next.val == val:
                currP.next = currP.next.next
            else:
                currP = currP.next
        
        return dummy_head.next