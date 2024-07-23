"""
https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1330438387/

TC: O(n)
SC: O(1)

Type: Linked List
"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prevNode = None
        ans = None

        while head and head.next:
            nextNextNode = head.next.next
            temp = head.next

            head.next = nextNextNode
            temp.next = head

            if prevNode:
                prevNode.next = temp
            else:
                ans = temp

            prevNode = head
            head = nextNextNode

        return ans
        
