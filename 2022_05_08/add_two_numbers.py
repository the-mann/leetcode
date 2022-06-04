# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # uh oh! must carry if greater than 10
        return self.twonums(l1, l2, False)

    def twonums(self, l1, l2, carry) -> Optional[ListNode]:
        if None not in [l1, l2]:
            s = l1.val + l2.val + (1 if carry else 0)
            return ListNode(val=s % 10, next=self.twonums(l1.next, l2.next, s >= 10))
        elif l1 == l2 == None:
            return ListNode(1) if carry else None
        else:
            # return whichever isn't none
            return self.finishCarry(l1 if l1 is not None else l2, carry)

    def finishCarry(self, l1, carry):
        if carry:
            if l1 is None:
                l1 = ListNode(0)
            nv = (l1.val + 1)
            x = self.finishCarry(l1.next, nv > 9)
            if l1.next is None:
                l1.next = x
            l1.val = nv % 10
        return l1