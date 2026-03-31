# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode()
        dummy.next = head

        prev, curr = dummy, head

        while curr:
            if length - n == 0:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            n += 1

        return dummy.next