import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

tomato = []

for _ in range(N):
    tomato.append(list(map(int, input().split())))

queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])



deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]


while queue:

    i, j = queue.popleft()

    for di, dj in deltas:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] != -1 and tomato[ni][nj] == 0:
            queue.append([ni, nj])
            tomato[ni][nj] = tomato[i][j] + 1

max_val = 0
answer = 0

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            answer = -1
            break

        max_val = max(max_val, tomato[i][j])


if max_val > 0 and answer != -1:
    answer = max_val - 1

print(answer)
