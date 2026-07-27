"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        print(intervals)
        till = 0
        for x in intervals:
            if x.start < till:
                return False
            else:
                till = x.end

        return True
