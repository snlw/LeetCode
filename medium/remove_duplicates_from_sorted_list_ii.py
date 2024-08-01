"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/1340403289/

TC: O(n)
SC: O(1)

Type: Linked List
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        ans = temp
        dup = None

        while head and head.next:
            currentValue = head.val
            nextValue = head.next.val

            if dup is not None and currentValue == dup:
                head = head.next
                continue

            if currentValue == nextValue:
                dup = currentValue
            else:
                dup = None
                temp.next = head
                temp = temp.next
            
            head = head.next

        if (dup is not None and head.val != dup) or (dup is None):
            temp.next = head
        else:
            temp.next = None
            
        return ans.next

