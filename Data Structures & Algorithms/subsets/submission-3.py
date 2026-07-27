class Solution:
    # recursive
    def subsets_1(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        first, *rest = nums

        s = self.subsets(rest)
        extra = []
        for x in s:
            extra.append([*x, first])
        return [*s, *extra]

    # none recursive 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        init = [[]]
        for n in nums:
            for item in init.copy():
                init.append([*item, n])
        return init
        