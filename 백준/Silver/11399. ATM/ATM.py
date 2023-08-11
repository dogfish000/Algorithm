N = int(input())

lst = list(map(int, input().split()))

lst.sort()

time = 0
for i in range(N):
    time += lst[i] * (N - i)

print(time)