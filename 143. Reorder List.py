# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

# solution using deque
# O(N) in time and additional memory
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get a list of the nodes
        node = head
        nodes = deque()
        while node:
            nodes.append(node)
            node = node.next
        
        # reorder them in a new list
        reordered = []
        start = True
        while nodes:
            if start:
                reordered.append(nodes.popleft())
            else:
                reordered.append(nodes.pop())
            start = not start
        
        # redo the pointers so the linked list reflect reordering
        froms = iter(reordered)
        tos = iter(reordered)
        next(tos) # safe because we know the list has at least one element
        while True:
            try:
                next(froms).next = next(tos, None)
            except StopIteration:
                break

# solution using only pointers
# O(N) in time, O(1) in additional memory
from math import ceil
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        if length < 3:
            return
        
        # cut the list into two halves
        pivot_index = int(ceil(length / 2)) -1
        before_pivot = head
        while pivot_index:
            pivot_index -= 1
            before_pivot = before_pivot.next
        pivot = before_pivot.next
        before_pivot.next = None
        
        # reverse the second half of the list
        node, child = pivot, pivot.next
        while child:
            grandchild = child.next
            child.next = node
            node, child = child, grandchild
        pivot.next = None
        head2 = node

        # zip the two halves back together
        node1, node2 = head, head2
        while node1:
            p = node1.next
            node1.next = node2
            node1 = p
            node1, node2 = node2, node1
