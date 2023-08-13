import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

sort_lst = sorted(lst)

dic = {}

idx = 0
for item in sort_lst:
    if item not in dic:
        dic[item] = idx
        idx += 1

ans_lst = []
for item in lst:
    ans_lst.append(dic[item])

print(*ans_lst)