class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sorted = [-1001] * k
        for n in nums:
            self.add_helper(n)

    def add_helper(self, val: int) -> int:
        for i, x in enumerate(self.sorted):
            if val > x:
                self.sorted[i+1:] = self.sorted[i:-1]
                self.sorted[i] = val
                break

    def add(self, val: int) -> int:
        self.add_helper(val)
        return self.sorted[-1]
        
        

        
