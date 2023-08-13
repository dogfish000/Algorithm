import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N, M = map(int, input().split())

campus = []
visited = []

for _ in range(N):
    campus.append(list(input().rstrip()))
    visited.append([0] * M)

cnt = 0

deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def scan_around(x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] == 1 or campus[x][y] == 'X':
            continue

        visited[x][y] = 1
        if campus[x][y] == 'P':
            global cnt
            cnt += 1

        for dx, dy in deltas:
            nx = x + dx
            ny = y + dy

            stack.append((nx, ny))




start_i = 0
start_j = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start_i = i
            start_j = j
            break

scan_around(start_i, start_j)

if cnt == 0:
    print("TT")
else:
    print(cnt)

