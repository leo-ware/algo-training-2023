# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# one pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        l = 0
        fast = head
        s = prev = None
        while fast:
            l += 1
            fast = fast.next
            if l >= n:
                s = getattr(s, "next", None) or head
            if l > n:
                prev = getattr(prev, "next", None) or head
        
        if prev and s:
            prev.next = s.next
        elif l == n:
            return head.next

        return head
