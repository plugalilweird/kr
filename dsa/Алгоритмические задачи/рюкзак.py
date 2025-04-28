def  knapsack(W, items_weights, items_prices):
    n = len(items_prices)

    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if  items_weights[i - 1] <= j:
                dp[i][j] = max(items_prices[i - 1] + dp[i - 1][j-items_weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp




print(knapsack(13, [3, 4, 5, 8, 9], [1, 6, 4, 7, 6]))
