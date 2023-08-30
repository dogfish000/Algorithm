import sys
input = sys.stdin.readline


N = int(input())

lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))


dp = []
for _ in range(N + 1):
    dp.append([0, 0, 0])


for i in range(1, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + lst[i - 1][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + lst[i - 1][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + lst[i - 1][2]

answer = min(dp[N][0], dp[N][1], dp[N][2])

print(answer)