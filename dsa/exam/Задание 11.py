#проходит

def solution(n, adjM):
    edges = set()

    for i in range(n):
        for j in range(n):
            if i != j and adjM[i][j] != float('inf'):
                edges.add((i, j, adjM[i][j]))

    return edges

