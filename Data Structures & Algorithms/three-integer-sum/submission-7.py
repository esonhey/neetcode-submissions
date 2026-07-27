class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[List[int]]:
        pairs = []
        l, r = 0, len(nums) - 1
        while l < r:
            pair_sum = nums[l] + nums[r]
            if pair_sum < t:
                l += 1
            elif pair_sum > t:
                r -= 1
            else:
                pairs.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
        return pairs

    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sets = set()
        nums.sort()
        for i in range(len(nums) - 2):
            for x in self.twoSum(nums[i+1:], -nums[i]):
                sets.add(tuple([nums[i], *x]))
        print(sets)
        return [list(x) for x in sets]
