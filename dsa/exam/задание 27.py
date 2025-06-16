#прошёл
import heapq

def solution(n, roads, s, p, A, B):
    """
    n     — число городов (0..n-1)
    roads — список кортежей (u, v) длины m
    s     — список длин дорог размера m
    p     — список пошлин размера m
    A, B  — номера начального и конечного города
    Возвращает минимальное S+P пути или None, если пути нет.
    """
    # Строим списки смежности с весом w = s[i] + p[i]
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(roads):
        w = s[i] + p[i]
        adj[u].append((v, w))
        adj[v].append((u, w))

    # Алгоритм Дейкстры
    dist = [float('inf')] * n
    dist[A] = 0
    heap = [(0, A)]
    while heap:
        d_u, u = heapq.heappop(heap)
        if u == B:
            return d_u  # как только извлечём B, это кратчайшее расстояние
        if d_u > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d_u + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return None  # B недостижим
