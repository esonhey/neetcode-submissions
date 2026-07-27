import math

[2, 1, 1, 1]

i = 2
minJumps = [0]



class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        minJumps = [0]
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums):
                minJumps.append(1)
            else:
                newMin = min(minJumps[len(minJumps) - nums[i]:] or [0])
                minJumps.append(newMin+1)
        return minJumps[-1]

            
        