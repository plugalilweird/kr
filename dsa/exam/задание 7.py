#выходит за время мб тесты кривые??
def solution(n, adjM):
    return {i: [j for j, val in enumerate(adjM[i]) if val] for i in range(n)}
