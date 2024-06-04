# https://leetcode.com/problems/reverse-linked-list/submissions/1277510624/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        values = []
        while head is not None:
            values.append(head.val)
            head = head.next

        reversedLinkedList = ListNode(values[-1])
        
        temp = reversedLinkedList

        for i in range(len(values) - 2, -1, -1):
            reversedLinkedList.next = ListNode(values[i])
            reversedLinkedList = reversedLinkedList.next

        return temp

        
