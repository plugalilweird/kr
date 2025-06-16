def solution(n, depend):
    # Строим граф и считаем входящие степени
    graph = [[] for _ in range(n)]
    in_degree = [0] * n

    for i in range(n):
        for dep in depend[i]:
            graph[dep].append(i)
            in_degree[i] += 1

    # Ищем процессы без зависимостей
    queue = [i for i in range(n) if in_degree[i] == 0]

    result = []
    while queue:
        process = queue.pop(0)
        result.append(process)

        for neighbor in graph[process]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Если не удалось обработать все процессы — значит, есть цикл
    if len(result) < n:
        return -1

    return result

