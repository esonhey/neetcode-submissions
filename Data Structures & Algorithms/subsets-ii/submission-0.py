class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dic = {}
        subsets = [[]]
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        
        for n, count in dic.items():
            oldsub = subsets.copy()
            for sub in oldsub:
                for c in range(1, count + 1):
                    subsets.append([*sub, *([n] * c)])
        return subsets