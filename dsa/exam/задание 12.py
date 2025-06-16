#прошёл
def solution(n, m, incM):
    edges = set()
    for j in range(m):
        source = None
        target = None
        for i in range(n):
            if incM[i][j] == -1:
                source = i
            elif incM[i][j] == 1:
                target = i
        if source is not None and target is not None:
            edges.add((source, target))
    return edges