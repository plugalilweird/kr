class Solution:
    def dfs(self, adj):
        N = len(adj)
        visited = [0] * N
        result = []

        def dfs1(v):
            visited[v] = 1
            result.append(v)
            for neigh in adj[v]:
                if not visited[neigh]:
                    dfs1(neigh)

        dfs1(0)
        return result