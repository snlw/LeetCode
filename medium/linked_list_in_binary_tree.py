"""
https://leetcode.com/problems/linked-list-in-binary-tree/submissions/1383305323/?envType=daily-question&envId=2024-09-07

TC: O(n * m), where n is the number of nodes in the LL and m is the number of nodes in the tree
SC: O(n)
"""
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(tree, head, curr):
            if curr is None:
                return True
            if tree is None:
                return False
            
            if tree.val == curr.val:
                curr = curr.next
            elif tree.val == head.val:
                head = head.next
            else:
                curr = head
               
            return dfs(tree.left, head, curr) or dfs(tree.right, head, curr)

        return dfs(root, head, head)
        
