class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(src, prev):
            if src in visited:
                return False

            visited.add(src)
            for ad in adj[src]:
                if ad == prev:
                    continue
                if not dfs(ad, src):
                    return False

            return True
        
        return dfs(0, -1) and n == len(visited)

        