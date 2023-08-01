stu_lst = []
room_cnt = 0

for _ in range(6):
    stu_lst.append([0, 0])

N, K = map(int, input().split())

for _ in range(N):
    S, Y = map(int, input().split())

    stu_lst[Y - 1][S] += 1


for items in stu_lst:
    for item in items:
        if item != 0:
            room_cnt += (item - 1)//K + 1

print(room_cnt)