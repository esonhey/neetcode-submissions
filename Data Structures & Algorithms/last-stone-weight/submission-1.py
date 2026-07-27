class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = sorted(stones)
        print(stones_heap)
        print('helllo')

        while len(stones_heap) > 1:
            l1 = stones_heap.pop()
            print('l1', l1, stones_heap)
            l2 = stones_heap.pop()
            print('l2', l2, stones_heap)
            if l1 == l2:
                continue
            else:
                stones_heap.append(l1 - l2)
                stones_heap.sort()
                print('after push', stones_heap)

        
        if not stones_heap:
            return 0
        return stones_heap[0]