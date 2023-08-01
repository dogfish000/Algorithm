N, X = map(int, input().split())
num_lst = list(map(int, input().split()))
out_lst = []

for i in range(N):
    if num_lst[i] < X:
        out_lst.append(num_lst[i])

for number in out_lst:
    print(number, end=" ")