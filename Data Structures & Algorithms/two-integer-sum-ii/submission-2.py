class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = (0, len(numbers) - 1)
        while start < end:
            sum1 = numbers[start] + numbers[end] 
            if sum1 == target:
                return [start+1, end+1]
            elif sum1 > target:
                end -= 1
            elif sum1 < target:
                start += 1
        return []