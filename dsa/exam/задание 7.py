def solution(n, adjM):
    result = {}
    for _ in range(n):
        result[_] = []

    for i in range(n):
        for j in range(i + 1, n):
            if adjM[i][j] == 1:
                result[i].append(j)
                result[j].append(i)
    return result