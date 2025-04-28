def dfs(xtqz):
    x = len(xtqz)
    s = 0
    visited = [0] * x
    stack = [0]
    while stack:
        ind = stack.pop()
        if not visited[ind]:
            s += 1
            visited[ind] = 1
            print(ind)
            for u in xtqz[ind]:
                if not visited[u]:
                    stack.append(u)
    print(s)
print(dfs(
    {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3]
    }
))




