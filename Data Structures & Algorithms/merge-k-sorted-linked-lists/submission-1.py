# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res

        heads = []

        for h in lists:
            if h:
                heads.append(h)

        while heads:
            lowestI = 0

            for h in range(1, len(heads)):
                if heads[h].val < heads[lowestI].val:
                    lowestI = h

            dummy.next = heads[lowestI]
            dummy = dummy.next 

            heads[lowestI] = heads[lowestI].next
            if not heads[lowestI]:
                heads.pop(lowestI)

        return res.next