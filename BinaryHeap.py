from heapq import heappush,heapify,heappop

class MiniHeap:
    #consturctor
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-2)/2

    def insert_key(self, key):
        heappush(self.heap, key)

    def decrease_key(self, i, new_val):
        self.heap[i] = new_val
        while i is not 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extra_min(self):
        return heappop(self.heap)

    def delete_key(self, i):
        self.decrease_key(i, float("-inf"))
        self.extra_min()

    def get_min(self):
        return self.heap[0]
