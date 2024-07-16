"""
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/submissions/1323031074/?envType=daily-question&envId=2024-07-16

TC: O(n)
SC: O(n)

Type: DFS, Backtracking, LCA
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath, destPath = [], []
        def dfs(root, target, pathFromRoot):
            if root is None:
                return []
            
            if root.val == target:
                return pathFromRoot
            pathFromRoot.append("L")
            leftTree = dfs(root.left, target, pathFromRoot)
            if leftTree == []:
                pathFromRoot.pop()
            pathFromRoot.append("R")
            rightTree = dfs(root.right, target, pathFromRoot)
            if rightTree == []:
                pathFromRoot.pop()

            return leftTree if leftTree else rightTree

        pathToStart = dfs(root, startValue, startPath)
        pathToDest = dfs(root, destValue, destPath)

        print(pathToStart, pathToDest)

        ## Remove common paths from root's POV
        ptr = 0
        while ptr < len(pathToStart) and ptr < len(pathToDest):
            if pathToStart[ptr] == pathToDest[ptr]:
                ptr += 1
            else:
                break
        pathToStart = pathToStart[ptr:]
        pathToDest = pathToDest[ptr:]

        pathFromStartToCommon = "U" * len(pathToStart)
        ans = pathFromStartToCommon + "".join(pathToDest)
        return ans
