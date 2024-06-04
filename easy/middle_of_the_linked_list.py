# https://leetcode.com/problems/middle-of-the-linked-list/submissions/1277529776/

# Time Complexity: O(n)
# Space Complexity: O(1)

# Type: Linked List, Hare-Tortoise Algorithm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and slow is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow
            
        
