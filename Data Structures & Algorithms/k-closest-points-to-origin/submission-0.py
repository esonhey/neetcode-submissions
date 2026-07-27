class Solution:
    def dist(self, point):
        x, y = point
        return ((x * x) + (y * y)) ** 0.5
        
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            distance = self.dist(point)
            heapq.heappush(heap,(-distance, point))

            if len(heap) > k:
                heapq.heappop(heap)

        return [x[1] for x in heap]
