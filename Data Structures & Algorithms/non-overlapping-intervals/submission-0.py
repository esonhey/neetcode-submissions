class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        activeIdx = 0
        delCount = 0
        while activeIdx < len(intervals) - 1:
            active = intervals[activeIdx]
            nextItem = intervals[activeIdx+1]
            if nextItem[0] >= active[1]:
                activeIdx +=1
                continue
            
            delCount += 1
            if nextItem[1] >= active[1]:
                del intervals[activeIdx+1]
            else:
                del intervals[activeIdx]
        
        return delCount
        


        