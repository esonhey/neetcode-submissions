class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            curr_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, curr_area)
            # diff1 = heights[l + 1] - heights[l]
            # diff2 = heights[r - 1] - heights[r]
            
            # print(diff1, diff2, heights[l], heights[r])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area