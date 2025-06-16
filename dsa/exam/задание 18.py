#тесты прошёл

from collections import deque




def solution(n: int, m: int, edges: list[tuple[int, int]]) -> bool:
    """
    Проверка ориентированного невзвешенного графа на ацикличность с помощью алгоритма Кана.

    Параметры:
    - n: число вершин (нумерация от 0 до n-1).
    - m: число рёбер.
    - edges: список рёбер (u, v) — направленное ребро из u в v.

    Возвращает True, если граф ацикличен, иначе False.
    """
    in_deg = [0] * n
    adj = [[] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        in_deg[v] += 1

    q = deque([i for i in range(n) if in_deg[i] == 0])
    count = 0

    while q:
        u = q.popleft()
        count += 1
        for w in adj[u]:
            in_deg[w] -= 1
            if in_deg[w] == 0:
                q.append(w)

    return count == n

