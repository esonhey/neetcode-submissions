class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]

        first, *rest = nums

        s = self.subsets(rest)
        extra = []
        for x in s:
            extra.append([*x, first])
        return [*s, *extra]
        