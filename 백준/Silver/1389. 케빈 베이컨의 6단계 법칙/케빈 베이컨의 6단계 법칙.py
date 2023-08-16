import sys
input = sys.stdin.readline


N, M = map(int, input().split())

dic = {}

for _ in range(M):
    s, e = map(int, input().split())

    dic[s] = dic.get(s, []) + [e]
    dic[e] = dic.get(e, []) + [s]

answer = []

for i in range(1, N + 1):
    dp = [N + 1] * (N + 1)
    dp[0] = 0
    dp[i] = 0

    stack = [i]
    visited = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in dic[v]:
                stack.append(w)
                dp[w] = min(dp[w], dp[v] + 1)

    answer.append(sum(dp))

min_val = min(answer)

idx = answer.index(min_val) + 1

print(idx)

