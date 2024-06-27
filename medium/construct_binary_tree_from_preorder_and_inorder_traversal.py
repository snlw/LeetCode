"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/1301731192/

Time Complexity: O(n**2)
Space Complexity: O(n)

Type: Binary Tree, Inorder Traversal (Left-Root-Right), Preorder Traversal (Root-Left-Right)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        self.idx = 0
        start = 0
        end = n - 1

        def build(start, end):
            if start > end:
                return None

            value = preorder[self.idx]
            node = TreeNode(value)
            self.idx += 1

            if start == end:
                return node

            position = [i for i in range(n) if inorder[i] == value][0]

            node.left = build(start, position - 1)
            node.right = build(position + 1, end)

            return node

        return build(start, end) 

