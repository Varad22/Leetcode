# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=n=ListNode(0)
        num1=[]
        num2=[]
        while l1 is not None:
            num1.append(str(l1.val))
            l1=l1.next
        while l2 is not None:
            num2.append(str(l2.val))
            l2=l2.next
        finalNum1 = int("".join(num1)[::-1])
        finalNum2 = int("".join(num2)[::-1])
        total = str(finalNum1+finalNum2)
        total = total[::-1]
        for i in total:
            d.next = ListNode(i)
            d = d.next
        return n.next
