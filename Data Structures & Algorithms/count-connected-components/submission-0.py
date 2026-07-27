class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        connected_count = 0

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(i, prev):
            if i in visited:
                return True
            
            visited.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                dfs(nei, i)
            return False


        for i in range(n):
            if not dfs(i, -1):
                connected_count += 1

        return connected_count
        