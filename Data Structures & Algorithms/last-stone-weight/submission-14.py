class Solution:
    def lastStoneWeight_v1(self, stones: List[int]) -> int:
        stones_heap = sorted(stones)
        print(stones_heap)
        print('helllo')

        while len(stones_heap) > 1:
            l1 = stones_heap.pop()
            l2 = stones_heap.pop()
            if l1 == l2:
                continue
            else:
                stones_heap.append(l1 - l2)
                stones_heap.sort()
        
        if not stones_heap:
            return 0
        return stones_heap[0]

    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            l1 = heapq.heappop(stones)
            l2 = heapq.heappop(stones)
            if l1 < l2:
                heapq.heappush(stones, l1 - l2)
        
        if not stones:
            return 0
        return -stones[0]
