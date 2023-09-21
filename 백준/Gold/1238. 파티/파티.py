import sys
from collections import deque
input = sys.stdin.readline

N, M, X = map(int, input().split())

edges = {}

for _ in range(M):
    s, e, k = map(int, input().split())
    edges[s] = edges.get(s, []) + [[e, k]]

dist = [987654321] * (N + 1)


def measure_route(start, end):
    copy_dist = dist.copy()
    copy_dist[start] = 0

    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        if v in edges:
            for item in edges[v]:
                nv, nk = item[0], item[1]
                if copy_dist[nv] > copy_dist[v] + nk:
                    copy_dist[nv] = copy_dist[v] + nk
                    q.append(nv)

    return copy_dist[end]

max_val = 0

for i in range(1, N + 1):
    if i != X:
        a = measure_route(i, X)
        b = measure_route(X, i)
        max_val = max(max_val, a + b)


print(max_val)
