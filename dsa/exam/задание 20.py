import heapq


def solution(n, roads):
    adj = [[] for _ in range(n)]
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))

    def dijkstra(start):
        dist = [float('inf')] * n
        dist[start] = 0
        heap = [(0, start)]

        while heap:
            d_u, u = heapq.heappop(heap)
            if d_u > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d_u + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))
        return dist

    best_city = 0
    best_sum = float('inf')
    for city in range(n):
        total = sum(dijkstra(city))
        if total < best_sum:
            best_sum = total
            best_city = city
    return best_city