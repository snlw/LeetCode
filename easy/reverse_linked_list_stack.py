# https://leetcode.com/problems/reverse-linked-list/submissions/1277520758/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Linked List, Stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next

        reversedLinkedListHead = ListNode(stack.pop())

        temp = reversedLinkedListHead
        
        while stack:
            reversedLinkedListHead.next = ListNode(stack.pop())
            reversedLinkedListHead = reversedLinkedListHead.next

        return temp    
