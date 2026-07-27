class MedianFinder:

    def __init__(self):
        self.median = None
        self.count = 0
        self.leftMaxHeap = [] # negating on insertion and pop
        self.rightMinHeap = []
        
    def addNum(self, num: int) -> None:
        if self.median == None:
            self.median = num
        
        else:
            if self.count % 2 == 1:
                if num > self.median:
                    heapq.heappush(self.leftMaxHeap, -self.median)
                    heapq.heappush(self.rightMinHeap, num)
                    headOfRight = self.rightMinHeap[0]
                    self.median = (self.median + headOfRight) / 2
                else:
                    heapq.heappush(self.rightMinHeap, self.median)
                    heapq.heappush(self.leftMaxHeap, -num)
                    head_of_left = -self.leftMaxHeap[0]
                    self.median = (self.median + head_of_left) / 2
            else:
                if num > self.median:
                    self.median = heapq.heappushpop(self.rightMinHeap, num)
                    
                else:
                    self.median = -heapq.heappushpop(self.leftMaxHeap, -num)                

        self.count += 1
        

    def findMedian(self) -> float:
        return self.median
        
        