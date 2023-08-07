import sys
input = sys.stdin.readline

N = int(input())

my_dict = {}

lstN = list(map(int, input().split()))

for num in lstN:
    tmp = my_dict.setdefault(num, 0)
    my_dict[num] += 1

M = int(input())

lstM = list(map(int, input().split()))

answer_lst = []

for num in lstM:
    tmp = my_dict.setdefault(num, 0)
    answer_lst.append(my_dict[num])

print(*answer_lst)
