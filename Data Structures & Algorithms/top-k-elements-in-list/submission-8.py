class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [(0, 0)] * k
        count = {}
        for n in nums:
            newCount = count.get(n, 0)+ 1
            count[n] = newCount

            for idx, (key, value) in enumerate(res):
                if value > newCount:
                    pass
                if newCount > value:
                    if key != n:
                        if (n, newCount -1) in res[idx:]:
                            res[idx+1:] = [x for x in res[idx:] if x[0] != n]
                        else:
                            res[idx+1:] = res[idx:-1] 
                    res[idx] = (n, newCount)
                    break
        print(count)
        return [x[0] for x in res if x[1]>0]
        
