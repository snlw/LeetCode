class Solution:
    def minPatches(self, nums, n):
        patch = 0
        dp = [False for _ in range(n + 1)]

        for num in nums:
            for i in range(1, n + 1):
                if dp[i] == True and i + num <= n:
                    dp[i + num] = True

            dp[num] = True

        print(dp)

        needPatch = [i for i in range(1, n + 1) if dp[i] == False]

        distance = set()

        for i in needPatch:
            for j in range(i, 0, -1):
                if dp[j] == True:
                    distance.add(i - j)
                    print(i, j)
                    break
        print(distance)
        return len(distance)

if __name__ == "__main__":
    sol = Solution()
    ans = sol.minPatches([1,3], 6)
    print(ans)
