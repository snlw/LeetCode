"""
https://leetcode.com/problems/design-linked-list/submissions/1331474858/

Type: Linked List
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.root = Node(-1)

    def get(self, index: int) -> int:
        head = self.root.next
        for _ in range(index):
            head = head.next
            if head is None:
                return -1
        if head:
            return head.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        existingHead = self.root.next
        newHead = Node(val)
        self.root.next = newHead
        self.root.next.next = existingHead

    def addAtTail(self, val: int) -> None:
        newTail = Node(val)
        tail = self.root
        while tail.next is not None:
            tail = tail.next
        
        tail.next = newTail

    def addAtIndex(self, index: int, val: int) -> None:
        head = self.root
        for _ in range(index):
            head = head.next
            if head is None:
                return
        node = Node(val)
        existing = head.next
        head.next = node
        head.next.next = existing
        
    def deleteAtIndex(self, index: int) -> None:
        head = self.root
        for _ in range(index):
            head = head.next
            if head is None:
                return
        if head.next is not None:
            head.next = head.next.next
