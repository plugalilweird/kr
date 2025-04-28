def biba_and_boba(n, m, g):
    adj = {i:[] for i in range(n)}
    for i, j in g:
        adj[i-1].append(j-1)
        adj[j-1].append(i-1)

    visited = [0] * n
    comp = []

    def dfs(u):
        visited[u] = 1
        comp[-1]+= 1
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
    for x in range(n):
        if not visited[x]:
            comp.append(0)
            dfs(x)
    return comp

print(
    (
    biba_and_boba(10, 6, [[1,2], [2,3], [3,4], [4,5], [6,7], [9,10]]),
    biba_and_boba(2, 1, [[1,2]])
    )
)