class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodeConnections = defaultdict(list)
        for t in times:
            nodeConnections[t[0]].append((t[1], t[2]))
        visited = set()
        visitedEdges = set()
        timer = -1
        ongoing = [(k, 1)]
        while ongoing and len(visited) < n and timer < 1000:
            new_ons = []
            closestOngoing = ongoing[0][1]
            for on in ongoing:
                new_on = (on[0], on[1] - closestOngoing)
                if new_on[1] == 0: # we are at on[1]
                    visited.add(on[0])
                    for edge in nodeConnections[on[0]]:
                        if edge not in visitedEdges:
                            visitedEdges.add(edge)
                            new_ons.append((edge[0], edge[1]))
                else:
                    new_ons.append(new_on)
            ongoing = sorted(new_ons, key=lambda x: x[1])
            timer += closestOngoing

        return timer if len(visited) == n else -1
        