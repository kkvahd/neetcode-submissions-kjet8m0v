# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptrs = []
        res = ListNode()
        dummy = res

        for i in lists:
            if i:
                ptrs.append(i)
        
        while ptrs:
            lowest = 0

            for p in range(1, len(ptrs)):
                if ptrs[p].val < ptrs[lowest].val:
                    lowest = p

            dummy.next = ptrs[lowest]
            dummy = dummy.next

            ptrs[lowest] = ptrs[lowest].next
            if not ptrs[lowest]:
                ptrs.pop(lowest)

        return res.next
