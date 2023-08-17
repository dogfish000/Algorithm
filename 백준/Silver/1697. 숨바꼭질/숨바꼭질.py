from collections import deque

N, K = map(int, input().split())

dp = [100001] * 100001
dp[K] = 0


def find_route(start):
    queue = deque()
    queue.append(start)

    while queue:
        v = queue.popleft()
        if v == N:
            return dp[v]

        l = v - 1
        r = v + 1

        if 0 <= l <= 100000 and dp[l] == 100001:
            dp[l] = dp[v] + 1
            queue.append(l)
        if 0 <= r <= 100000 and dp[r] == 100001:
            dp[r] = dp[v] + 1
            queue.append(r)
        if v % 2 == 0:
            x = v // 2
            
            if 0 <= x <= 100000 and dp[x] == 100001:
                dp[x] = dp[v] + 1
                queue.append(x)

a = find_route(K)
print(a)