# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# https://leetcode.com/problems/linked-list-cycle/submissions/1276180995/

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Hash Map
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head

        s = set()

        while (temp != None):
            if temp in s:
                return True

            s.add(temp)
            temp = temp.next
        
        return False

        
