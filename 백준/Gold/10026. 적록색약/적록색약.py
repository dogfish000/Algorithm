import sys, copy
from collections import deque
input = sys.stdin.readline

N = int(input())

normal_lst = []
for _ in range(N):
    normal_lst.append(list(input().rstrip()))

handi_lst = copy.deepcopy(normal_lst)

for i in range(N):
    for j in range(N):
        if handi_lst[i][j] == 'R':
            handi_lst[i][j] = 'G'


deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def normal_RGB(i, j, lst):
    queue = deque()
    queue.append([i, j])

    while queue:
        i, j = queue.popleft()

        if lst[i][j] == 'R':
            lst[i][j] = 'D'
            for di, dj in deltas:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 'R':
                    queue.append([ni, nj])

        if lst[i][j] == 'G':
            lst[i][j] = 'D'
            for di, dj in deltas:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 'G':
                    queue.append([ni, nj])

        if lst[i][j] == 'B':
            lst[i][j] = 'D'
            for di, dj in deltas:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 'B':
                    queue.append([ni, nj])

    global normal_cnt
    normal_cnt += 1


def handi_RGB(i, j, lst):
    queue = deque()
    queue.append([i, j])

    while queue:
        i, j = queue.popleft()


        if lst[i][j] == 'G':
            lst[i][j] = 'D'
            for di, dj in deltas:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 'G':
                    queue.append([ni, nj])

        if lst[i][j] == 'B':
            lst[i][j] = 'D'
            for di, dj in deltas:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 'B':
                    queue.append([ni, nj])

    global handi_cnt
    handi_cnt += 1


normal_cnt = 0
handi_cnt = 0
for i in range(N):
    for j in range(N):
        if normal_lst[i][j] in ['R', 'G', 'B']:
            normal_RGB(i, j, normal_lst)
        if handi_lst[i][j] in ['G', 'B']:
            handi_RGB(i, j, handi_lst)


print(normal_cnt, handi_cnt)




