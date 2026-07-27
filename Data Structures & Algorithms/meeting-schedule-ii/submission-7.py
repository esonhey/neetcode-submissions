"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        s = e = c = res = 0
        while s < len(starts):
            if ends[e] <= starts[s]:
                c -= 1
                e += 1
                continue
            s += 1
            c += 1
            res = max(c, res)
        return res

    def minMeetingRooms1(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        layers = []
        for interval in intervals:
            if not layers:
                layers.append([interval])
                continue
            hasOverlap = False
            for idx, ls in enumerate(layers):
                hasOverlap = False
                for l in ls:
                    if l.start >= interval.end or l.end <= interval.start:
                        continue
                    else:
                        hasOverlap = True
                        break
                if not hasOverlap:
                    layers[idx].append(interval)
                    break
                continue
            if hasOverlap:
                layers.append([interval])

        return len(layers)
        


        