"""
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/submissions/1385338435/?envType=daily-question&envId=2024-09-10

TC: O(n) where n is the number of nodes in the linked list
SC: O(n)
"""
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int):
            big = max(a, b)
            small = min(a, b)
            while big % small:
                euclid_rem = big % small
                big = small 
                small = euclid_rem
            return small

        ans = head
        while head is not None and head.next is not None:
            first_node = head
            second_node = head.next
            section_gcd = gcd(first_node.val, second_node.val)
            insert_node = ListNode(section_gcd, second_node)
            first_node.next = insert_node
            head = head.next.next

        return ans
