"""
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/submissions/1310171416/?envType=daily-question&envId=2024-07-05

Time Complexity: O(n log n)
Space Complexity: O(n / 2)

Type: Linked List
"""
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        
        critical = []

        if len(values) < 3:
            return [-1, -1]

        def isLocalMaxima(i):
            return values[i - 1] < values[i] and values[i] > values[i + 1]
        
        def isLocalMinima(i):
            return values[i - 1] > values[i] and values[i] < values[i + 1]

        for i in range(1, len(values) - 1):
            if isLocalMinima(i) or isLocalMaxima(i):
                critical.append(i)

        if len(critical) < 2:
            return [-1, -1]

        maxDistance = critical[-1] - critical[0]
        minDistance = sorted([ abs(critical[i] - critical[i + 1]) for i in range(len(critical) - 1)])[0]

        return [minDistance, maxDistance]


