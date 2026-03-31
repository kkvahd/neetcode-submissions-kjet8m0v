# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        res = ListNode()

        p1, p2, pRes = list1, list2, res

        while p1 != None and p2 != None:
            v1 = p1.val
            v2 = p2.val

            if v1 <= v2:
                pRes.next = p1
                p1 = p1.next
            else:
                pRes.next = p2
                p2 = p2.next
            pRes = pRes.next

        while p1 != None:
            pRes.next = p1
            p1 = p1.next
            pRes = pRes.next

        while p2 != None:
            pRes.next = p2
            p2 = p2.next
            pRes = pRes.next

        return res.next
        