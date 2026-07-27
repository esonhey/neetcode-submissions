class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        x = 0
        while start <= end and x < 10:
            target = (end + start) // 2
            x += 1
            if end - start < 2:
                return min(nums[end], nums[start])
            if (nums[target] <= nums[target - 1]):
                return nums[target]
                
            print('start ', nums[start], ' ,end ', nums[end])
            if nums[end] < nums[start] and nums[target] > nums[start]:
                start = target + 1
            else:
                end = target - 1
        return 0
        