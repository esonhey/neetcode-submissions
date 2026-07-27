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

        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        init = [[]]
        for n in nums:
            copy = init.copy()
            for item in copy:
                init.append([*item, n])
        return init
        