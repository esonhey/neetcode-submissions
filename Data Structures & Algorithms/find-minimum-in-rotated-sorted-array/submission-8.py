class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            target = (end + start) // 2
            if end - start < 2:
                return min(nums[end], nums[start])

            if (nums[target] <= nums[target - 1]):
                return nums[target]
                
            if nums[target] > nums[end]:
                start = target + 1
            else:
                end = target - 1
        