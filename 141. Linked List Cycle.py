
# exploit the fast that list has a max length of 10^4
# O(1) time and memory
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        for _ in range(10001):
            if node is None:
                return False
            node = node.next
        return True

# fast and slow pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
