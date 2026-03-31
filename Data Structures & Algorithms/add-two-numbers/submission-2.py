# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        p1, p2 = l1, l2

        carry = 0
        while p1 or p2:
            num1 = p1.val if p1 else 0
            num2 = p2.val if p2 else 0

            add = num1 + num2 + carry

            if add >= 10:
                carry = 1 
                add = add % 10
            else:
                carry = 0
            res.next = ListNode(add)

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            res = res.next

        if carry:
            res.next = ListNode(carry)

        return dummy.next
