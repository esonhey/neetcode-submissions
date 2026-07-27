def findIdx(arr, fn):
    res = []
    print('arr', arr)
    for i, x in enumerate(arr):
        if fn(x):
            res.append(i)
    return res

def isAdj(p1):
    def res(p2):
        v = ((p1[0] - p2[0] == 0) and (abs(p2[1] - p1[1]) == 1)) or ((abs(p1[0] - p2[0]) == 1) and (p2[1] - p1[1] == 0))
        return v
    return res

class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                adjs = [idx for idx, points in enumerate(res) if len([*filter(isAdj([i, j]), points)]) > 0]
                if not adjs:
                    res.append([[i, j]])
                elif len(adjs) == 1:
                    res[adjs[0]].append([i, j])

                else:
                    merged = [[i, j]]
                    for t in adjs:
                        merged = merged + res[t]
                    res[adjs[0]] = merged
                    for t in adjs[-1:0:-1]:  
                        del res[t]

        return len(res)

        