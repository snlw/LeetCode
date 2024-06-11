# https://leetcode.com/problems/relative-sort-array/submissions/1284595969

# Time Complexity: O(n)
# Space Complexity: O(n)

# Type: Hash Map
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        frequency = dict()

        for i in range(n):
            if arr1[i] in frequency.keys():
                frequency[arr1[i]] += 1
            else:
                frequency[arr1[i]] = 1

        newArr = [] 
        m = len(arr2)
        for i in range(m):
            for _ in range(frequency[arr2[i]]):
                newArr.append(arr2[i])

        notInArr2 = sorted([ele for ele in arr1 if ele not in arr2])

        return newArr + notInArr2

