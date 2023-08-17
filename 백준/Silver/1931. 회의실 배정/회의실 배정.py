import sys
input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    a, b = map(int, input().split())

    lst.append([a, b])

lst.sort(key=lambda x: (x[1], x[0]))

start_time = 0
cnt = 0

for item in lst:
    if item[0] >= start_time:
        cnt += 1
        start_time = item[1]

print(cnt)