import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    lst.append(list(map(int, input().rstrip())))

cnt_house = 0
num_house_lst = []

deltas = [(1, 0), (-1, 0), (0, 1), (0, - 1)]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    lst[i][j] = 2
    visited = []

    while queue:
        i, j = queue.popleft()
        visited.append([i, j])
        for di, dj in deltas:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and lst[ni][nj] == 1:
                lst[ni][nj] = 2
                queue.append([ni, nj])

    global cnt_house
    cnt_house += 1
    return len(visited)



for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            num_house_lst.append(bfs(i, j))

print(cnt_house)
num_house_lst.sort()

for i in range(len(num_house_lst)):
    print(num_house_lst[i])




