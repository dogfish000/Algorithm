lst = [[0] * 100 for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            lst[i][j] = 1



cnt = 0

for items in lst:
    for item in items:
        if item == 1:
            cnt +=1

print(cnt)