import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap, res, n = [(matrix[0][0], 0, 0)], 0, len(matrix)
        for k in range(1, k + 1):
            res, row, col = heapq.heappop(heap)
            if not row and col < n - 1:
                heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
            if row < n - 1:
                heapq.heappush(heap, (matrix[row + 1][col], row + 1, col))
        return res
