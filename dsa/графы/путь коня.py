def find_knight_path(n, knightPos, targetPos):
    distance = [[float('inf')]*n for _ in  range(n)]
    distance[knightPos[0] - 1][knightPos[1] - 1] = 0
    queue = [(knightPos[0] - 1, knightPos[1] - 1)]
    while queue:
        i, j = queue.pop(0)
        possible_moves = [(i-1, j-2), (i-1, j+2), (i-2, j+1), (i-2, j-1), (i+1, j-2), (i+1, j+2), (i+2, j-1), (i+2, j+1)]
        for i1,j1 in possible_moves:
            if 0<=i1<n and 0<=j1<n:
                if distance[i1][j1] > distance[i][j]+1:
                    distance[i1][j1] = distance[i][j]+1
                    queue.append((i1, j1))
                    if i1 == targetPos[0] - 1 and j1 == targetPos[1] - 1:
                        return distance[i1][j1]
    if distance[targetPos[0] - 1][targetPos[1] -1] == float('inf'):
        return -1
    return distance[targetPos[0] - 1][targetPos[1] - 1]




print(find_knight_path(6, (4,5), (1,1)), find_knight_path(2, (1, 1), (2, 2)))