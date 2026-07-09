# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        first , second = headA , headB
        firstl , secondl = 0 , 0
        while first:
            first = first.next
            firstl += 1
        while second:
            second = second.next
            secondl += 1
        
        while headA and headB:
            if firstl > secondl:
                headA = headA.next
                firstl -= 1
            elif firstl < secondl:
                headB = headB.next
                secondl -= 1
            else:
                if headB == headA:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
                    firstl -=1
                    secondl -= 1
        return None