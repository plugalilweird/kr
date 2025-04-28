def editorial_dist(a, b):
    n, m = len(a), len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1 ):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                if i == 1 and j == 1:
                    dp[i][j] = 1
                    continue
                op = []
                if i > 1:
                    op.append(dp[i-1][j])
                if j > 1:
                    op.append(dp[i][j-1])
                if j > 1 and i > 1:
                    op.append(dp[i - 1][j - 1])

                dp[i][j] = min(op) + 1


    return dp

print(editorial_dist("мяу", "вау"))