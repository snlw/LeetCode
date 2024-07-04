"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1309613025/

Time Complexity: O(n2)
Space Complexity: O(1)

Type: Linked List
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        temp2 = head
        ans = head
        nodes = 0

        while temp is not None:
            temp = temp.next
            nodes += 1
        
        if nodes == n:
            head = head.next
            return head

        while temp2 is not None:
            if nodes == n + 1:
                if n == 1:
                    temp2.next = None
                else:
                    temp2.next = temp2.next.next
                break
            temp2 = temp2.next
            nodes -= 1
            
        return ans
        
