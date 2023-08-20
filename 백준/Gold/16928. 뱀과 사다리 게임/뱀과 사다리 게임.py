import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())

dic = {}

for _ in range(N + M):
    a, b = map(int, input().split())

    dic[a] = b


dp = [101] * 101
dp[1] = 0

def bfs(start, dp):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        if v == 100:
            break



        if v in dic:
            queue.append(dic[v])
            if dp[dic[v]] > dp[v]:
                dp[dic[v]] = dp[v]

        else:
            for i in range(1, 7):
                a = v + i
                if a <= 100 and dp[a] > dp[v] + 1:
                    dp[a] = dp[v] + 1
                    queue.append(a)


bfs(1, dp)

print(dp[100])


