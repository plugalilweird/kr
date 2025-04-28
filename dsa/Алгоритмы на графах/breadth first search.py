def bfs(xtqz):
    x = len(xtqz)
    visited = [0] * x
    visited[0] = 1

    queue = [0]

    while queue:
        v = queue.pop(0)

        for u in xtqz[v]:
            if not visited[u]:
                visited[u] = 1
                queue.append(u)
        print(queue)
print(bfs(
    {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
    }
))