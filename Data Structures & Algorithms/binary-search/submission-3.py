class Solution:
    def search_v1(self, nums: List[int], target: int, offset = 0) -> int:
        if not nums: return -1
        pointer = int(len(nums) / 2)
        if nums[pointer] == target:
            return pointer + offset
        if nums[pointer] < target:
            return self.search(nums[pointer+1:], target, offset+pointer+1)
        else:
            return self.search(nums[:pointer], target, offset)
    
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1

        while s <= e:
            pointer = (s + e) // 2
            if nums[pointer] == target:
                return pointer
            if nums[pointer] < target:
                s = pointer + 1
            else:
                e = pointer - 1
        return -1