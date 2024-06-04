# https://leetcode.com/problems/flood-fill/submissions/1277200064/

# Time Complexity: O(m * n)
# Space Complexity: O(1)

# Type: Recursion, DFS

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        currentColor = image[sr][sc]

        if color == currentColor:
            return image

        # Change current pixel to desired color
        image[sr][sc] = color

        # Check left
        if sc - 1 >= 0 and image[sr][sc - 1] == currentColor:
            self.floodFill(image, sr, sc - 1, color)

        # Check right
        if sc + 1 < n and image[sr][sc + 1] == currentColor:
            self.floodFill(image, sr, sc + 1, color)

        # Check up
        if sr - 1 >= 0 and image[sr - 1][sc] == currentColor:
            self.floodFill(image, sr - 1, sc, color)

        # Check down
        if sr + 1 < m and image[sr + 1][sc] == currentColor:
            self.floodFill(image, sr + 1, sc, color)

        return image
        
        
