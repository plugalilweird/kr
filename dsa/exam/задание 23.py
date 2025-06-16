#гпт, прошёл
from collections import deque


def solution(n: int, depend: list[list[int]]) -> list[int] or int:
    """
    Находит порядок выполнения n процессов с учётом зависимостей.

    Параметры:
    - n: количество процессов (нумерация от 0 до n-1).
    - depend: список списков, где depend[i] — процессы, от которых зависит i.

    Возвращает любой допустимый порядок (список из n индексов) или -1, если топологическая сортировка невозможна.
    """
    in_deg = [0] * n
    adj = [[] for _ in range(n)]

    # Строим граф: из каждой зависимости j->i
    for i in range(n):
        for j in depend[i]:
            adj[j].append(i)
            in_deg[i] += 1

    # Инициализируем очередь независимых процессов
    q = deque([i for i in range(n) if in_deg[i] == 0])
    order = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)

    # Проверяем, все ли процессы учтены
    return order if len(order) == n else -1

