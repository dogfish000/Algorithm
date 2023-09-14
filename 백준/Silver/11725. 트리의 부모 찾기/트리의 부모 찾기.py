import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dic = {}

for _ in range(N - 1):
    a, b = map(int, input().split())
    dic[a] = dic.get(a, []) + [b]
    dic[b] = dic.get(b, []) + [a]

# print(dic)

visited = [0] * (N + 1)
parent_idx = [0] * (N + 1)

queue = deque()
queue.append(1)

while queue:
    i = queue.popleft()
    visited[i] = 1
    if i in dic:
        for ni in dic[i]:
            if visited[ni] == 0:
                queue.append(ni)
                parent_idx[ni] = i

for i in range(2, N + 1):
    print(parent_idx[i])