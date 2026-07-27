class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        startIsDone = False
        endIsDone = False
        res = []
        for s, e in intervals:
            if endIsDone:
                res.append([s, e])
                continue
            
            if not startIsDone:
                if start > s:
                    if start > e: 
                        res.append([s, e])
                        continue
                    if end <= e:
                        res.append([s, e])
                        endIsDone = True
                        startIsDone = True
                        continue
                    # start > s and end > e
                    
                    start = s
                    startIsDone = True
                    continue
            # start is done
            if s > end:
                res.append([start, end])
                res.append([s, e])
                endIsDone = True
                continue
            end = max(end, e)

        if not endIsDone:
            res.append([start, end])
        return res




        