from heapq import heappush, heappop
from collections import Counter


class Solution(object):
    """
    Given a char array representing tasks CPU need to do.
    It contains capital letters A to Z where different letters represent different tasks.
    Tasks could be done without original order. Each task could be done in one interval. For each interval,
    CPU could finish one task or just be idle.
    However, there is a non-negative cooling interval n that means between two same tasks,
    there must be at least n intervals that CPU are doing different tasks or just be idle.
    """
    def least_interval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        curr_time, h = 0, []
        for k,v in Counter(tasks).items():
            heappush(h, (-1*v, k))
        while h:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return curr_time

    def least_interval2(self, tasks, n):
        import collections
        d = collections.Counter(tasks)
        values = d.values()
        most = max(values)
        value_count = collections.Counter(values)
        return max((most - 1) * (n + 1) + value_count[most], len(tasks))
