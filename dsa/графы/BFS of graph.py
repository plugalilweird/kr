class Solution:
    def bfs(self, adj):
        N = len(adj)
        visited = [0] * N
        result = []
        queue = []

        queue.append(0)
        visited[0] = 1

        while queue:
            v = queue.pop(0)
            result.append(v)

            for neigh in adj[v]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    queue.append(neigh)

        return result