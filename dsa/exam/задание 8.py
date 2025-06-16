#прошел
def solution(n, m, adjL):


    edges = set()

    for u in adjL:
        for v in adjL[u]:
            edges.add((u, v))

    return edges

print(solution(3, 3, {0: [1, 2], 1: [2], 2: []}))