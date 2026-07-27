class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = -1001
        acc = 0
        for n in nums:
            if acc + n < 0:
                acc = 0
                maxSub = max(maxSub, n)
            else:
                acc += n
                maxSub = max(maxSub, acc)
        return maxSub
        