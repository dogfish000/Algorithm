import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if H != 1:
    deltas.append((N, 0))
    deltas.append((-N, 0))

tomato = []

for _ in range(N * H):
    tomato.append(list(map(int, input().split())))

queue = deque()

for i in range(N * H):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])


def bfs(H):
    if H == 1:
        while queue:
            i, j = queue.popleft()
            for di, dj in deltas:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] == 0:
                    queue.append([ni, nj])
                    tomato[ni][nj] = tomato[i][j] + 1

    else:
        while queue:
            i, j = queue.popleft()
            for di, dj in deltas:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N * H and 0 <= nj < M and tomato[ni][nj] == 0:
                    if (di, dj) in [(1, 0), (-1, 0)]:
                        if (ni // N) != (i // N):
                            continue

                    queue.append([ni, nj])
                    tomato[ni][nj] = tomato[i][j] + 1


bfs(H)

answer = 0
max_val = 0

for i in range(N * H):
    for j in range(M):
        if tomato[i][j] == 0:
            answer = -1
            break

        if tomato[i][j] > max_val:
            max_val = tomato[i][j]

if answer == 0 and max_val > 1:
    answer = max_val - 1


print(answer)