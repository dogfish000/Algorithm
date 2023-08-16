import sys
from collections import deque
input = sys.stdin.readline

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input().rstrip())))


def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited = []
    while queue:
        i, j = queue.popleft()
        visited.append([i, j])
        for di, dj in deltas:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and [ni, nj] not in visited:
                queue.append([ni, nj])
                maze[ni][nj] = maze[i][j] + 1

bfs(0, 0)

print(maze[N -1][M - 1])



