"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node'], oldToNew = {}) -> Optional['Node']:
        if node in oldToNew: return oldToNew[node]
        if not node: 
            oldToNew[node] = None
            return None

        copy = Node(node.val)
        oldToNew[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(self.cloneGraph(n, oldToNew))

        return copy
        
        