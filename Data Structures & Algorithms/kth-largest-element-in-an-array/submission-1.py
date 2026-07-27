class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)

        for i in range(k):
            h = heapq.heappop(heap)
        return -h
