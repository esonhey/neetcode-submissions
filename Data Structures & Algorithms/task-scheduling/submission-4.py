import heapq 
from collections import deque


class Solution:
    def countByLetter(self, tasks: List[str]):
        counts = {}
        for s in tasks:
            counts[s] = counts.get(s, 0) + 1
        return counts.values()

    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = self.countByLetter(tasks)
        maxHeap = []
        for c in counts:
            heapq.heappush(maxHeap, -c)
        queue = deque()
        cycle = 0
        while maxHeap or queue:
            if maxHeap:
                curr = heapq.heappop(maxHeap)
                if curr < -1:
                    queue.append((curr + 1, cycle + n))
            if queue and queue[0][1] == cycle:
                heapq.heappush(maxHeap, queue.popleft()[0])
            cycle += 1
        return cycle











    ## first solution on second attempt
    def findNextPossibleChar(self, counted, tasks_min_cycle, cycle, n):
        i = len(counted) - 1
        while i >= 0:
            for c in counted[i]:
                if tasks_min_cycle.get(c, 0) < cycle:
                    tasks_min_cycle[c] = cycle + n
                    counted[i] = counted[i].replace(c, '')
                    if i == len(counted) - 1 and counted[i] == '':
                        del counted[i]
                    if (i>0):
                        counted[i-1] += c

                    return c
            i -= 1
        return None
        
    def _leastInterval(self, tasks: List[str], n: int) -> int:
        counted = countByLetter(tasks)
        tasks_min_cycle = {}
        cycle = 0
        while counted: 
            cycle +=1
            self.findNextPossibleChar(counted, tasks_min_cycle, cycle, n)
        return cycle
            
        

def countByLetter(strs: List[str]):
    counted = ['']
    visited = set([])
    for c in strs:
        if c not in visited:
            counted[0] += c
            visited.add(c)
            continue

        for idx, list_of_char in enumerate(counted):
            if c in list_of_char:
                counted[idx] = counted[idx].replace(c, '')
                if (len(counted) - 1 == idx):
                    counted.append(c)
                else:
                    counted[idx+1] += c
                break

    return counted
    