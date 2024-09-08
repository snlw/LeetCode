"""
https://leetcode.com/problems/split-linked-list-in-parts/submissions/1383285705/?envType=daily-question&envId=2024-09-08

TC: O(n)
SC: O(k)
"""
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k

        length = 0 
        dummy = head
        while dummy is not None:
            length += 1
            dummy = dummy.next
        
        partSize = length // k 
        rem = length % k 

        current = head
        for i in range(k):
            ans[i] = current
            currentSize = partSize
            if rem:
                currentSize += 1
                rem -= 1
            
            for _ in range(currentSize - 1):
                current = current.next
            
            if current:
                newHead = current.next
                current.next = None
                current = newHead
        return ans
