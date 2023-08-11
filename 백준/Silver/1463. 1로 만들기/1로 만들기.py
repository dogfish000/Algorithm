N = int(input())

dp = [N] * (N + 1)


dp[1] = 0

for i in range(1, N):
    if i * 3 <= N:
        if dp[i * 3] > dp[i] + 1:
            dp[i * 3] = dp[i] + 1

    if i * 2 <= N:
        if dp[i * 2] > dp[i] + 1:
            dp[i * 2] = dp[i] + 1

    if i + 1 <= N:
        if dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1

print(dp[N])