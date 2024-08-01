"""
https://leetcode.com/problems/linked-list-cycle-ii/submissions/1340341102/

TC: O(n)
SC: O(1)

Type: Linked List, Floyd's Cycle Algorithm
"""
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast

        return None
        
