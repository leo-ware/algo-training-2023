import heapq as hq

counter = 0
def to_ord(node):
    global counter
    counter += 1
    return (node.val, counter, node)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [to_ord(n) for n in lists if n]
        hq.heapify(heap)
        head = node = ListNode()

        while heap:
            node.next = hq.heappop(heap)[2]
            node = node.next
            if node.next:
                hq.heappush(heap, to_ord(node.next))
            node.next = None
        
        head = head.next
        return head
