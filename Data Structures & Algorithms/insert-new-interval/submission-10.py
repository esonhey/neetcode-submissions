class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []
        done = False
        for s, e in intervals:
            if done:
                res.append([s, e])
                continue
            if end < s:
                res.append([start, end])
                res.append([s, e])
                done = True
                continue
            
            if start > e:
                res.append([s, e])
                continue

            start = min(s, start)
            end = max(e, end)
        
        if not done:
            res.append([start, end])
            
        return res




        