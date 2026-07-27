class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1] * len(nums)
        print(out)
        p = 1
        for i, n in enumerate(nums):
            print("j", i)
            out[i] = p 
            p *= n
        p = 1
        for i in range(len(nums)-1,-1, -1):
            out[i] *= p
            p *= nums[i]
        return out