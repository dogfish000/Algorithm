import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append([W, V])

dp = [-1] * (K + 1)

dp[0] = 0

for item in items:
    tmp_w, tmp_v = item[0], item[1]
    tmp_lst = []
    copy_dp = dp.copy()
    for i in range(0, K + 1 - tmp_w):
        if dp[i] != -1:
            tmp_lst.append(i)

    for idx in tmp_lst:
        if copy_dp[idx + tmp_w] < copy_dp[idx] + tmp_v:
            dp[idx + tmp_w] = copy_dp[idx] + tmp_v


print(max(dp))