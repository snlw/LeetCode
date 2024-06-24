"""
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/submissions/1298838846

Time Complexity: O(n)
Space Complexity: O(1)

Type: Sliding Window

Editorial: 
The main idea is to maintain a variable currentFlips that represents the number of flips in the current sliding window of size k, to decide whether we need to perform a flip or not.

If currentFlips is even and nums[i] is 0, we need to flip the bit. Similarly, if currentFlips is odd and nums[i] is 1, we also need to flip the bit. We use the parity of currentFlips (whether it's even or odd) to determine if the current bit needs flipping.

To perform a flip, we mark the current bit by setting nums[i] to 2, increment currentFlips, and increase totalFlips. As the window slides, if the element at the start of the previous window (i - k) was flipped (i.e., it was set to 2), we decrement currentFlips.

If flipping the current bit would go beyond the array bounds (i.e., i + k exceeds the array size), we return -1 as it is impossible to make all elements 1.
"""
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # Greedy encounters TLE
        n = len(nums)

        currentFlips = 0
        totalFlips = 0

        for i in range(n):
            if i >= k and nums[i - k] == 2:
                currentFlips -= 1

            if currentFlips % 2 == nums[i]:
                if i + k > n:
                    return -1
                nums[i] = 2
                currentFlips += 1
                totalFlips += 1
        return totalFlips

        
