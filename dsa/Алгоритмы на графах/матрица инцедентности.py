incMat = [
    [1, 1, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0],
]



def adjList_to_incMat(adj):
    incMatr = set()
    for i in adj:
        for j in adj[i]:
            tmp = [0] * len(adj)
            tmp[i] = 1
            tmp[j] = 1
            incMatr.add (tuple(tmp))
    result = [[0]*len(incMatr)for _ in range(len(adj))]
    incMatr = list(incMatr)
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = incMatr[j][i]


    return result





print(adjList_to_incMat({
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
}))