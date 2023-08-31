import sys
import copy
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())


lst = [list(map(int, input().split())) for _ in range(N)]


def dfs(cnt, input_lst):
    global max_val

    if cnt == 3:
        tmp = bfs(input_lst)
        max_val = max(max_val, tmp)
        return


    for i in range(N):
        for j in range(M):
            if input_lst[i][j] == 0:
                input_lst[i][j] = 1
                dfs(cnt + 1, input_lst)
                input_lst[i][j] = 0


def bfs(input_lst):
    copy_lst = copy.deepcopy(input_lst)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if copy_lst[i][j] == 2:
                queue.append([i, j])

    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cnt = 0
    while queue:
        i, j = queue.popleft()
        for di, dj in deltas:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and copy_lst[ni][nj] == 0:
                copy_lst[ni][nj] = 2
                queue.append([ni, nj])

    for i in range(N):
        for j in range(M):
            if copy_lst[i][j] == 0:
                cnt += 1

    return cnt


max_val = -1
dfs(0, lst)

print(max_val)


