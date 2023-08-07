N = int(input())

set1 = set(list(map(int, input().split())))

M = int(input())

lst2 = list(map(int, input().split()))

for i in range(M):
    if lst2[i] in set1:
        print(1)
    else:
        print(0)