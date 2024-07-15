"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/1321905832/?envType=study-plan-v2&envId=leetcode-75

TC: O(n)
SC: O(1)

Type: Linked List
"""
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head
        tortoise, hare = head, head
        prev = None

        ## Scenario: Linked List has single node 
        if tortoise.next is None:
            return None

        while hare.next is not None:
            prev = tortoise
            tortoise = tortoise.next
            hare = hare.next
            if hare.next is not None:
                hare = hare.next
            else:
                break
        
        ## Remove middle node
        prevNode = prev
        middleNode = tortoise
        nextNode = tortoise.next
        middleNode.next = None
        prevNode.next = nextNode

        return ans

        
