"""
https://leetcode.com/problems/binary-tree-right-side-view/submissions/1316184795/

TC: O(height)
SC: O(height*2)

Type: DFS, Recursion
"""
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(nodes):
            if len(nodes) == 0 or nodes[-1] is None:
                return
            ans.append(nodes[-1].val)
            nextLevel = []
            for node in nodes:
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
            
            return dfs(nextLevel)
        
        dfs([root])

        return ans
