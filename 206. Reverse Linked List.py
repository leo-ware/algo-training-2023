# O(N) time and memory
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        node = head
        while node:
            lst.append(node)
            node = node.next
        
        if len(lst) < 2:
            return head
        else:
            for a, b in zip(lst[1:], lst):
                a.next = b
            lst[0].next = None
            return a

# recursive solution
# also O(N) time and memory because Python doesn't have tail recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(h, c):
            g = c.next
            c.next = h
            if g:
                return reverse(c, g)
            else:
                return c

        if not head or not head.next:
            return head
        head.next, child = None, head.next
        return reverse(head, child)

# iterative solution
# O(N) time, O(1) additional memory
class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        if not h or not h.next:
            return h
        h.next, c = None, h.next

        while True:
            g = c.next
            c.next = h
            if not g:
                return c
            h, c = c, g
