#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(None)
        current = dummyHead
        carry = 0
        while l1 or l2 or carry:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if carry:
                num += carry
                carry -= 1
            carry, num = num % 10
            current.next = ListNode(num)
            current = current.next
        return dummyHead.next
