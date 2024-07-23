"""
https://leetcode.com/problems/rotate-list/submissions/1330767093/

TC: O(n ^ 2)
SC: O(1)

Type: Linked List
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        length = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            length += 1
        
        cutoff = length - k % length
        if cutoff == 0 or cutoff == length:
            return head
        
        temp = head
        while cutoff > 1:
            temp = temp.next
            cutoff -= 1

        ans = temp.next
        temp.next = None
        tail.next = head
        
        return ans

