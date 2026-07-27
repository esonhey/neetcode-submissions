class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        res = []
        for i, c in enumerate(nums):
            x = self.permute(nums[:i] + nums[i+1:])
            for j in x:
                res.append([c, *j])
        return res
