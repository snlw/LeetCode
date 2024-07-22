"""
https://leetcode.com/problems/sort-the-people/submissions/1329052718/?envType=daily-question&envId=2024-07-22

TC: O(n)
SC: O(n)

Type: Sort
"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peopleWithHeights = sorted(zip(names, heights), key=lambda x:x[1], reverse=True)
        return [people[0] for people in peopleWithHeights]
        
