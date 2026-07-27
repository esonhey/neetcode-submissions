class Solution:
    def __init__(self):
        self.hashmap = set()

    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if n in self.hashmap:
                return n
            self.hashmap.add(n)


        