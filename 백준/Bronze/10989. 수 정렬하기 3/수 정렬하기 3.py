import sys
input = sys.stdin.readline

N = int(input())
cnt_lst = [0] * 10000

for _ in range(N):
    a = int(input())
    cnt_lst[a - 1] += 1
    

for i in range(10000):
    if cnt_lst[i] != 0:
        for j in range(cnt_lst[i]):
            print(i + 1)
