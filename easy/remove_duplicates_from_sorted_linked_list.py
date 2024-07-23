"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1330728057/

TC: O(n)
SC: O(1)

Type: Linked List
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = head

        while head and head.next:
            currentValue = head.val
            nextValue = head.next.val
            if currentValue == nextValue:
                if head.next.next:
                    head.next = head.next.next
                else:
                    head.next = None
                    break
            else:
                head = head.next

        return ans
        
