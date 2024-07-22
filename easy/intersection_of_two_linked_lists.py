"""
https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/1329651424/

TC: O(n + m)
SC: O(1)

Type: Linked List
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tempA = headA
        tempB = headB

        lengthA, lengthB = 1, 1
        tailA, tailB = None, None

        ## Move linked lists to their tails
        while headA is not None:
            if headA.next is None:
                tailA = headA.val
            headA = headA.next
            lengthA += 1
        
        while headB is not None:
            if headB.next is None:
                tailB = headB.val
            headB = headB.next
            lengthB += 1
        
        if tailA != tailB:
            return None
        
        if lengthA > lengthB:
            diff = lengthA - lengthB
            for _ in range(diff):
                tempA = tempA.next
        else:
            diff = lengthB - lengthA
            for _ in range(diff):
                tempB = tempB.next

        while(tempA != tempB):
            tempA = tempA.next
            tempB = tempB.next

        return tempA
        


        
