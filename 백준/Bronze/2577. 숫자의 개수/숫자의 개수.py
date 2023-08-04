A = int(input())
B = int(input())
C = int(input())

cnt_lst = [0] * 10

N = A * B * C

while N >= 1:
    a = N % 10
    cnt_lst[a] += 1

    N = N // 10

for i in range(10):
    print(cnt_lst[i])