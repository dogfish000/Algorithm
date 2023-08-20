import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())

lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))


start_i = 0
start_j = 0

for i in range(N):
    for j in range(M):
        if lst[i][j] == 2:
            start_i = i
            start_j = j
            lst[i][j] = 0

        elif lst[i][j] == 1:
            lst[i][j] = N * M + 1


deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(start_i, start_j, lst):
    queue = deque()
    queue.append([start_i, start_j])

    while queue:
        i, j = queue.popleft()

        for di, dj in deltas:
            ni = i + di
            nj = j + dj

            if 0 <= ni < N and 0 <= nj < M and lst[ni][nj] == N * M + 1:
                queue.append([ni, nj])
                lst[ni][nj] = lst[i][j] + 1



bfs(start_i, start_j, lst)

for i in range(N):
    for j in range(M):
        if lst[i][j] == N * M + 1:
            lst[i][j] = -1



for i in range(N):
    print(*lst[i])


