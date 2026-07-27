class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        if nums[0] == target:
            return 0
        while s < e:
            mid = (s + e) // 2
            curr = nums[mid] 
            print(nums[s], curr, nums[e])
            if curr == target:
                return mid
            if nums[s] == target:
                return s
            if nums[e] == target:
                return e

            if curr > nums[e]:
                if target < nums[s] or target > nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
            else:
                if target < nums[s]:
                    e = mid - 1
                else:   
                    s = mid + 1
        return -1

        