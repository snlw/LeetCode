class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        n = len(nums)
        ## Boolean to determine if number of zeros is 1
        encountered = False

        left, right = 0, 0
        ans = -1

        while right < n:
            if nums[right] == 0:
                if not encountered:
                    encountered = True
                else:
                    while left < n:
                        if nums[left] == 0:
                            left += 1
                            break
                        left += 1
                    encountered = False
            right += 1
            ans = max(ans, right - left)

        return ans
