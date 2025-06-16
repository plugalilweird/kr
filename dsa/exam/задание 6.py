#прошёл
def solution(n, m, edges):
    adjacency_list = {}
    for i in range(n):
        adjacency_list[i] = []

    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    return adjacency_list