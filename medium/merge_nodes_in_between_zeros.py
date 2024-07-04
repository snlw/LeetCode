"""
https://leetcode.com/problems/merge-nodes-in-between-zeros/submissions/1309463329/?envType=daily-question&envId=2024-07-04

Time Complexity: O(n)
Space Complexity: O(n)

Type: Linked List
"""
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []

        while head is not None:
            if head.val == 0 and head.next is not None:
                values.append(0)
            else:
                values[-1] += head.val
            head = head.next

        startNode = ListNode(values[0])
        temp = startNode

        for i in range(1, len(values)):
            newNode = ListNode(values[i])
            startNode.next = newNode
            startNode = startNode.next

        return temp
