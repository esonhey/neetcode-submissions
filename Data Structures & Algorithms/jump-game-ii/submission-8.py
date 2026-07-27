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
                newMin = float("inf")
                for x in range(1, nums[i]+1):
                    newMin = min(newMin, minJumps[len(minJumps) - x])
                minJumps.append(newMin+1)
        return minJumps[-1]

            
        