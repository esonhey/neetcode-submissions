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
        startIdx = 0
        endIdx = 0
        count = 0
        maxCount = 0
        while startIdx < len(starts):
            if ends[endIdx] <= starts[startIdx]:
                count -= 1
                endIdx += 1
                continue
            startIdx += 1
            count += 1
            if count > maxCount:
                maxCount = count
        return maxCount



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
        


        