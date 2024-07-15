"""
https://leetcode.com/problems/create-binary-tree-from-descriptions/submissions/1321344106/?envType=daily-question&envId=2024-07-15

TC: O(n) --> Building the map == Finding the root == Calling DFS on each node are all O(n)
SC: O(n)

Type: Recursion, Binary Tree, DFS
"""
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        adj = dict()
        possibleRoots = set()
        children = set()
        for parent, child, isLeft in descriptions:
            key = 'L' if isLeft else 'R'
            if parent in adj:
                adj[parent][key] = child
            else:
                adj[parent] = { key: child }
            
            if child not in adj:
                adj[child] = {}

            children.add(child)
            if child in possibleRoots:
                possibleRoots.remove(child)
            if parent not in children:
                possibleRoots.add(parent)

        root = TreeNode(list(possibleRoots)[0])

        def build(node):
            ## Find children
            branches = adj[node.val]
            
            if "L" in branches:
                node.left = TreeNode(branches["L"])
                build(node.left)
            
            if "R" in branches:
                node.right = TreeNode(branches["R"])
                build(node.right)
            
            return

        build(root)
        return root

