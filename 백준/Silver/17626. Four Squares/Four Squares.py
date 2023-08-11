n = int(input())

dp = [n] * (n + 1)

range_num = int(n ** 0.5 + 1)

for i in range(1, range_num):
    dp[i * i] = 1


for i in range(1, n):
    if dp[i] == 1:

        for j in range(1, range_num):
            if i + j * j <= n and dp[i] + 1 < dp[i + j * j]:
                dp[i + j * j] = dp[i] + 1

for i in range(1, n):
    if dp[i] == 2:

        for j in range(1, range_num):
            if i + j * j <= n and dp[i] + 1 < dp[i + j * j]:
                dp[i + j * j] = dp[i] + 1

for i in range(1, n):
    if dp[i] == 3:

        for j in range(1, range_num):
            if i + j * j <= n and dp[i] + 1 < dp[i + j * j]:
                dp[i + j * j] = dp[i] + 1

print(dp[n])