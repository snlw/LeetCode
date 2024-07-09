"""
https://leetcode.com/problems/average-waiting-time/submissions/1314859790/?envType=daily-question&envId=2024-07-09

TC: O(n)
SC: O(1)

Type: Simulation
"""
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total = 0
        start = customers[0][0]

        for arrival, time in customers:
            if arrival <= start:
                ## Customer has to wait for previous order to be completed
                total += start - arrival
            else:
                ## For non-overlapping case
                start = arrival

            total += time
            start += time

        return total / n
