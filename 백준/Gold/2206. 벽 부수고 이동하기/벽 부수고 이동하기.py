import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

lst = []
dp = []
for _ in range(N):
    lst.append(list(map(int, input().rstrip())))
    dp.append([[99999999, 99999999]for _ in range(M)])

# print(dp)
# print(lst)
dp[0][0] = [1, 1]

queue = deque()

deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue.append([0, 0, 0])


while queue:
    i, j, wall = queue.popleft()

    for di, dj in deltas:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M:
            if lst[ni][nj] == 0:
                if dp[ni][nj][wall] > dp[i][j][wall] + 1:
                    dp[ni][nj][wall] = dp[i][j][wall] + 1
                    queue.append([ni, nj, wall])
            else:
                if wall == 0 and dp[ni][nj][wall + 1] > dp[i][j][wall] + 1:
                    dp[ni][nj][wall + 1] = dp[i][j][wall] + 1
                    queue.append([ni, nj, wall + 1])



answer = min(dp[N - 1][M - 1])
if answer == 99999999:
    answer = -1
print(answer)