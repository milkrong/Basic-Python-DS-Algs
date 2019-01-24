import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res, heap = [], []
        for item in lists:
            while item:
                heapq.heappush(heap, item.val)
                item = item.next

        while heap:
            res.append(heapq.heappop(heap))

        return res