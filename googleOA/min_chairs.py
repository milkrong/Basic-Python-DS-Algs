import heapq

class Solution(object):
    def min_chair(self, start, end):
        e = res = 0
        heap = []
        start = sorted(start)
        end = sorted(end)
        for s in range(len(start)):
            if start[s] < end[e]:
                res += 1
            else:
                e += 1
        return res

s = Solution()
res = s.min_chair([1,2,6,5,3], [5,5,7,6,8])
print(res)