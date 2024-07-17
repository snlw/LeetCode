"""
https://leetcode.com/problems/delete-nodes-and-return-forest/submissions/1323810769/?envType=daily-question&envId=2024-07-17

TC: O(n)
SC: O(n)

Type: DFS
"""
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        nodes = []

        def dfs(root, isRoot):
            if root is None:
                return
            toDeleteCurrentNode = root.val in to_delete
            if isRoot and not toDeleteCurrentNode:
                nonlocal nodes
                nodes.append(root)
                
            leftNode, rightNode = root.left, root.right
            if leftNode and leftNode.val in to_delete:
                root.left = None

            if rightNode and rightNode.val in to_delete:
                root.right = None

            dfs(leftNode, isRoot = toDeleteCurrentNode)
            dfs(rightNode, isRoot = toDeleteCurrentNode)

            return

        dfs(root, isRoot = True)
        return nodes

