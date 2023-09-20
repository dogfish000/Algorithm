import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dist = [[]]

lst = []

for _ in range(N):
    tmp_lst = list(map(int, input().split()))
    lst.append(tmp_lst)

lst.sort()

for item in lst:
    tmp_lst = []
    for l in range(1, len(item), 2):
        if item[l] != -1:
            tmp_lst2 = []
            tmp_lst2.append(item[l])
            tmp_lst2.append(item[l + 1])
            tmp_lst.append(tmp_lst2)
    dist.append(tmp_lst)

def find_route(start):
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        for item in dist[v]:
            e = item[0]
            k = item[1]
            if dp[e] == 0 and e != start:
                dp[e] = dp[v] + k
                q.append(e)

dp = [0] * (N + 1)

find_route(1)

max_idx = dp.index(max(dp))

dp = [0] * (N + 1)

find_route(max_idx)

answer = max(dp)

print(answer)


