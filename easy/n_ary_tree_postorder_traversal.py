"""
https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1369062173/?envType=daily-question&envId=2024-08-26

TC: O(n)
SC: O(n)

Type: DFS
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(node):
            if node is None:
                return
            
            if node.children:
                for child in node.children:
                    dfs(child)

            ans.append(node.val)
        dfs(root)
        return ans
            
