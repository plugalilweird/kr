def find_islands(grid):
    def dfs(i, j):
        grid[i][j] = 0
        list_near_vers = [
            (i + 1, j),
            (i, j + 1),
            (i - 1, j),
            (i, j - 1),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j - 1),
            (i + 1, j + 1),
        ]
        for i1, j1 in list_near_vers:
            if i1 >= 0 and j1 >= 0 and i1 < len(grid) and j1 < len(grid[0]):
                if grid[i1][j1] == 1:
                    dfs(i1, j1)

    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                cnt += 1
                dfs(i, j)
    return cnt


print(
    find_islands([[0, 1], [1, 0], [1, 1], [1, 0]]),
    find_islands(
        [
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 1],
        ]
    ),
)
