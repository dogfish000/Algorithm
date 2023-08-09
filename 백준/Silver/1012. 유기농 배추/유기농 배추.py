import sys
sys.setrecursionlimit(99999)

input = sys.stdin.readline

T = int(input())

deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def search_around(i, j, visited, lst):
    if i < 0 or i >= M or j < 0 or j >= N:
        return

    if lst[i][j] == 1 and visited[i][j] == 0:
        visited[i][j] = 1

        for dx, dy in deltas:
            search_around(i + dx, j + dy, visited, lst)


for tc in range(1, T + 1):
    M, N, K = map(int, input().split())

    lst = []
    visited = []

    for _ in range(M):
        lst.append([0] * N)
        visited.append([0] * N)

    for _ in range(K):
        x, y = map(int, input().split())

        lst[x][y] = 1

    cnt = 0

    for i in range(M):
        for j in range(N):
            if lst[i][j] == 1 and visited[i][j] == 0:
                search_around(i, j, visited, lst)
                cnt += 1

    print(cnt)
