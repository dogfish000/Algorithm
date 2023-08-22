import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j, cnt, val, visited):
    global max_val
    # 종료
    if val + (4 - cnt) * 1000 < max_val:
        return

    # 종료
    if cnt == 4:
        max_val = max(max_val, val)
        return

    # 실행
    for di, dj in deltas:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in visited:
            visited.append([ni, nj])
            bfs(ni, nj, cnt + 1, val + lst[ni][nj], visited)
            visited.remove([ni, nj])

def bfs_2(i, j, cnt, val, deltas, visited):
    global max_val
    # 종료
    if val + (4 - cnt) * 1000 < max_val:
        return

    if cnt == 4:
        max_val = max(max_val, val)
        return

    # 실행
    for di, dj in deltas:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and [ni, nj] not in visited:
            visited.append([ni, nj])
            bfs_2(i, j, cnt + 1, val + lst[ni][nj], deltas, visited)
            visited.remove([ni, nj])


max_val = 0

for i in range(N):
    for j in range(M):
        bfs(i, j, 1, lst[i][j], [[i, j]])
        bfs_2(i, j, 1, lst[i][j], deltas, [[i, j]])

print(max_val)

