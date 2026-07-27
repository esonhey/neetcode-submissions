class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target == 0: return [[]]
        if target < 1 or not nums: return []

        first, *rest = nums
        with_ = self.combinationSum(nums, target - first)
        without_ = self.combinationSum(rest, target)
        return [*map(lambda x: [*x, first], with_), *without_]
        