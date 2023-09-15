import sys

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
# print(lst)

dp = [1] * N
dp_rev = [1] * N

dp[0] = 1

for i in range(1, N):
    tmp_max = 1
    for j in range(i - 1, -1, -1):
        if lst[j] < lst[i]:
            tmp_max= max(tmp_max, dp[j] + 1)
        dp[i] = tmp_max

for i in range(N - 2, -1, -1):
    tmp_max = 1
    for j in range(i + 1, N):
        if lst[i] > lst[j]:
            tmp_max = max(tmp_max, dp_rev[j] + 1)
        dp_rev[i] = tmp_max


answer = 0

for i in range(N):
    answer = max(answer, dp[i] + dp_rev[i] - 1)

print(answer)