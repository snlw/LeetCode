# https://leetcode.com/problems/k-closest-points-to-origin/submissions/1278263096/

# Time Complexity: O(n + k log n)
# Space Complexity: O(n)

# Type: Arrays

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceCoordinatesTupleList = []
        for point in points:
            distance = self.getEuclideanDistanceFromOrigin(point)
            distanceCoordinatesTupleList.append((distance, point))

        distanceCoordinatesTupleList.sort(key=lambda tup: tup[0]) 
        
        return [point for _, point in distanceCoordinatesTupleList[:k]]

    def getEuclideanDistanceFromOrigin(self, coordinate: List[int]):
        a, b = coordinate
        return a*a + b*b
        
