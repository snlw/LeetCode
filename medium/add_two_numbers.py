"""
https://leetcode.com/problems/add-two-numbers/submissions/1303130928/

Time Complexity: O(max(m,n))
Space Complexity: O(max(m,n))

Type: Linked List
"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total, a, b = 0, 0, 0
        while l1 is not None:
            total += l1.val * 10**a
            a += 1
            l1 = l1.next 

        while l2 is not None:
            total += l2.val * 10**b
            b += 1
            l2 = l2.next 
        
        ## Init first node
        rem = total % 10 
        ans = ListNode(rem)
        total = total // 10

        temp = ans

        while total > 0:
            node = ListNode(total % 10)
            total = total // 10
            ans.next = node
            ans = ans.next

        return temp
        
