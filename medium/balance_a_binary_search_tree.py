"""
https://leetcode.com/problems/balance-a-binary-search-tree/submissions/1300977406/?envType=daily-question&envId=2024-06-26

Time Complexity: O(height)
Space Complexity: O(n)

Type: Binary Search Trees, Inorder Traversal
"""
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        
        # Perform an inorder traversal to store the elements in sorted order
        def inOrderTraversal(root, arr):
            if root is None:
                return
            inOrderTraversal(root.left, arr)
            arr.append(root.val)
            inOrderTraversal(root.right, arr)

        inOrderTraversal(root, inorder)

        def createBST(inorder, start, end):
            if start > end:
                return

            # Get middle element 
            mid = start + (end - start) // 2

            # Construct left and right
            left = createBST(inorder, start, mid - 1)
            right = createBST(inorder, mid + 1, end)

            # Construct current node with left and right subtrees
            node = TreeNode(inorder[mid], left, right)
            return node

        return createBST(inorder, 0, len(inorder) - 1)
