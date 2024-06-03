# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/linked-list-cycle/submissions/1276160819/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Floyd’s cycle-finding algorithm, Two Pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head

        while hare != None and tortoise != None and hare.next != None:
            hare = hare.next.next
            tortoise = tortoise.next

            if (hare == tortoise):
                return True
        
        return False
        
