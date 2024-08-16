"""
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/submissions/1357529058/

TC: O(n)
SC: O(1)
"""
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head is not None:
            ans = 2 * ans + head.val
            head = head.next

        return ans
