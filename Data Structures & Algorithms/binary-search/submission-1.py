class Solution:
    def search(self, nums: List[int], target: int, offset = 0) -> int:
        if not nums: return -1
        pointer = int(len(nums) / 2)
        if nums[pointer] == target:
            return pointer + offset
        if nums[pointer] < target:
            return self.search(nums[pointer+1:], target, offset+pointer+1)
        else:
            return self.search(nums[:pointer], target, offset)