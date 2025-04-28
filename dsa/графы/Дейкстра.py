class Solution:
    def dijkstra(self, V, edges, src):
        result = [float('inf')] * V
        result[src] = 0
        set_visited = set()
        dict_adj = {i: [] for i in range(V)}

        for i,j,weight in edges:
            dict_adj[i].append((j, weight))
            dict_adj[j].append((i, weight))

        def normal_edges():
            index_normal = 0
            for index in range(V):
                if index not in set_visited and result[index] != float('inf') and result[index] < result[index_normal]:
                    index_normal = index
            return index_normal

        for _ in range(V - 1):
            i = normal_edges()
            set_visited.add(i)
            for index,weight in dict_adj[i]:
                if index not in set_visited and result[index] > result[i] + weight:
                    result[index] = result[i] + weight
        return result
