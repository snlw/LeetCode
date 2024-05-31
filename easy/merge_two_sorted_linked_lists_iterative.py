# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1273083857/

# Time Complexity: O(n+m)
# Space Complexity: O(1)

# Type: Iterative

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        # Get all values in both LL
        for ll in [list1, list2]:
            while (ll is not None):
                values.append(ll.val)
                ll = ll.next
        
        if (len(values) == 0):
            return ListNode().next
        
        # Sort values
        values.sort()

        # Create first node in the newly-merged LL
        answer = ListNode(values[0])

        # Create a copy as the pointer in answer will move to the tail
        copy = answer

        for value in values[1:]:
            new_node = ListNode(value)
            answer.next = new_node
            answer = answer.next

        return copy

        
        
