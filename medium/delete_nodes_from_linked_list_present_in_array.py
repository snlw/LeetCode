"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/submissions/1325989483/

TC: O(n)
SC: O(1)

Type: Linked List
"""
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(-1)
        ansHead = ans
        remove = set(nums)
        while head is not None:
            if head.val not in remove:
                ansHead.next = head
                ansHead = ansHead.next

            head = head.next
        ansHead.next = None

        return ans.next
        
