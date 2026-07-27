class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        temp = None
        res = []
        for interval in intervals:
            if not temp:
                temp = interval
                continue
            if interval[0] <= temp[1]:
                temp = [min(interval[0], temp[0]), max(interval[1], temp[1])]
                continue
            res.append(temp)
            temp = interval
        res.append(temp)

        return res
        