def numRollsToTarget(n: int, k: int, target: int) -> int:
    # divid and conquer? -> dp from small to large
    # f(n, k, target) = f(n-1, k, targe-1) + f(n-1, k, target-2) + ... + f(n-1, k, target-k)
    dp = [[0] * (target + 1) for _ in range(n + 1)]  # dp[n][target]

    for row in range(1, n + 1):  # number of dices, also row
        for i in range(1, target + 1):  # target
            if row == 1 and i <= k:
                dp[row][i] = 1
            elif row == 1 and i > k:
                continue
            elif row * k < i:  # n > 1
                continue
            else:
                dp[row][i] = sum(
                    [dp[row - 1][i - cur] for cur in range(1, min(i, k + 1))]
                )
        print(dp[row])

    return dp[n][target]


numRollsToTarget(30, 30, 500)

