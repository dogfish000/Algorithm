import sys
input = sys.stdin.readline
import copy

R, C, T = map(int, input().split())

air_top = 0
air_bot = 0

lst = []

for _ in range(R):
    lst.append(list(map(int, input().split())))

for i in range(R):
    if lst[i][0] == -1:
        air_top = i
        air_bot = i + 1
        break

time = 0

deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while time < T :
    copied_lst = copy.deepcopy(lst)
    for i in range(R):
        for j in range(C):
            if copied_lst[i][j] >= 5:
                tmp_cnt = 0
                for di, dj in deltas:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and copied_lst[ni][nj] != -1:
                        lst[ni][nj] += copied_lst[i][j] // 5
                        tmp_cnt += copied_lst[i][j] // 5
                lst[i][j] -= tmp_cnt

    #위 반시계
    for i in range(air_top - 1, 0, -1):
        lst[i][0] = lst[i - 1][0]

    for i in range(0, C - 1):
        lst[0][i] = lst[0][i + 1]

    for i in range(0, air_top):
        lst[i][C - 1] = lst[i + 1][C - 1]

    for i in range(C - 1, 1, -1):
        lst[air_top][i] = lst[air_top][i - 1]
    lst[air_top][1] = 0

    # 아래 시계
    for i in range(air_bot + 1, R - 1):
        lst[i][0] = lst[i + 1][0]

    for i in range(0, C - 1):
        lst[R - 1][i] = lst[R - 1][i + 1]

    for i in range(R - 1, air_bot, -1):
        lst[i][C - 1] = lst[i - 1][C - 1]

    for i in range(C - 1, 1, -1):
        lst[air_bot][i] = lst[air_bot][i - 1]
    lst[air_bot][1] = 0


    # 시간
    time += 1


answer = 2
for i in range(R):
    answer += sum(lst[i])
    
print(answer)