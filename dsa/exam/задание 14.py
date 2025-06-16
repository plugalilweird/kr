#прошёл
def solution(N, M, edges):
    adjacency_list = {}

    for i in range(N):
        adjacency_list[i] = []
    for from_vertex, to_vertex in edges:
        adjacency_list[from_vertex].append(to_vertex)

    return adjacency_list