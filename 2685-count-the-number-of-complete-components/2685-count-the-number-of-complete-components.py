from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: set() for i in range(n)}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visited = set()
        def dfs(node, nodes, edges):
            visited.add(node)
            nodes.add(node)
            edges += len(adj[node])
            for neighbor in adj[node]:
                if neighbor not in visited:
                    edges = dfs(neighbor, nodes, edges)
            return edges

        count = 0
        for i in range(n):
            if i not in visited:
                nodes = set()
                edges = dfs(i, nodes, 0)
                if edges == len(nodes) * (len(nodes) - 1):
                    count += 1

        return count

        