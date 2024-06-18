"""
https://leetcode.com/problems/most-profit-assigning-work/submissions/1292496249

Time Complexity: O(n)
Space Complexity: O(n)

Type: Two Pointers
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)

        worker.sort()

        assignments = sorted(zip(difficulty, profit), key=lambda x:x[0])
        currentMaxDifficulty, currentMaxProfit = assignments[0]
        workerIdx = 0
        assignmentIdx = 0
        total = 0
        while workerIdx < len(worker):
            while currentMaxDifficulty <= worker[workerIdx] and assignmentIdx < n:
                if assignments[assignmentIdx][0] > worker[workerIdx] :
                    break
                currentMaxDifficulty = assignments[assignmentIdx][0]
                currentMaxProfit = max(currentMaxProfit, assignments[assignmentIdx][1])
                assignmentIdx += 1

            if worker[workerIdx] >= currentMaxDifficulty:
                total += currentMaxProfit

            workerIdx += 1

        return total
