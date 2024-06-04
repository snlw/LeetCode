# https://leetcode.com/problems/reverse-linked-list/submissions/1277516717/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Linked List, Iterative

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousNode = None
        currentNode = head

        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        return previousNode
        
