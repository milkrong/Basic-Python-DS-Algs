# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.
    :param intervals: list[intervals]
    :return:list[intervals]
    """
    if not intervals:
        return []

    res = []
    for i in sorted(intervals, key=lambda x: x.start):
        if res and i.start <= res[-1].end:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res.append(i)

    return res