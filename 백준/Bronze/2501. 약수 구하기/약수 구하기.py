N, K = map(int, input().split())

lst = []
answer = 0

for i in range(1, N + 1):
    if N % i == 0:
        lst.append(i)

if K > len(lst):
    print(answer)

else:
    print(lst[K - 1])



