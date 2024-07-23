"""
https://leetcode.com/problems/odd-even-linked-list/submissions/1330394108/

TC: O(n)
SC: O(1)

Type: Linked List
"""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1 -> 2 -> 3 -> 4 -> 5
        In 1st op:
            1 -//-> 2 -//-> 3 -> 4 -> 5
            1 -> 3 -> 4 -> 5 -> 2
        In 2nd op:
            1 -> 3 -//-> 4 -//-> 5 -> 2
            1 -> 3 -> 5 -> 2 -> 4
        """
        if head is None:
            return None

        ans, tail = head, head
        length = 1
        while tail.next is not None:
            tail = tail.next
            length += 1
        
        if length == 2:
            return ans
        
        numberOfOps = length // 2

        while numberOfOps:
            ## Disconnect even-placed node
            evenNode = head.next
            head.next = head.next.next
            head = head.next

            ## Connect removed node at the tail
            tail.next = evenNode
            tail = tail.next
            tail.next = None

            numberOfOps -= 1

        return ans


