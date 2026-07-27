class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        for s, e in intervals:
            if end == -1:
                res.append([s, e])
                continue
            if end < s:
                res.append([start, end])
                res.append([s, e])
                end = -1
                continue
            
            if start > e:
                res.append([s, e])
                continue

            start = min(s, start)
            end = max(e, end)
        
        if end != -1:
            res.append([start, end])
            
        return res




        