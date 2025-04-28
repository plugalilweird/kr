def adj_Mat_to_adjList(mat):
    graph = {}
    v = len(mat)
    for line in range(v):
        tmp = []
        for i in range(v):
            if mat[line][i]:
                tmp.append(i+1)
        graph [line + 1] = tmp
    return graph






adjMat = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
]



print(adj_Mat_to_adjList(adjMat))

