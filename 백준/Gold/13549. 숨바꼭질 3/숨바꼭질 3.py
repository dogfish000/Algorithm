from collections import deque

N, K = map(int, input().split())

lst = [987654321] * 100001
lst[N] = 0

q = deque()
q.append(N)
while q:
    v = q.popleft()
    if 0 <= v + 1 <= 100000 and lst[v + 1] > lst[v] + 1:
        lst[v + 1] = lst[v] + 1
        q.append(v + 1)

    if 0 <= v - 1 <= 100000 and lst[v - 1] > lst[v] + 1:
        lst[v - 1] = lst[v] + 1
        q.append(v - 1)

    if 2 * v <= 100000 and lst[2 * v] > lst[v]:
        lst[2 * v] = lst[v]
        q.append(2 * v)

print(lst[K])