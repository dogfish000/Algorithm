import sys

input = sys.stdin.readline

N, K = map(int, input().split())

lst = []

for _ in range(N):
    lst.append(int(input()))

lst.reverse()

cnt = 0

for coin in lst:
    if K // coin > 0:
        cnt += K // coin
        K = K % coin

print(cnt)