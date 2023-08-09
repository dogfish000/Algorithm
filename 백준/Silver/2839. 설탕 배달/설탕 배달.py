import sys
input = sys.stdin.readline

N = int(input())

cnt = 0

cnt += N // 5

N = N - (cnt * 5)

is_possible = 0

for i in range(cnt + 1):
    M = N + 5 * i
    if M % 3 == 0:
        cnt -= i
        cnt += M // 3
        is_possible = 1
        break

if is_possible:
    print(cnt)
else:
    print(-1)


