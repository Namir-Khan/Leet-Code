# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        currP = dummyHead

        while list1 and list2:
            if list1.val < list2.val:
                currP.next = list1
                currP = list1
                list1 = list1.next
            else:
                currP.next = list2
                list2, currP = list2.next, list2

        if list1 or list2:
            currP.next = list1 if list1 else list2

        return dummyHead.next