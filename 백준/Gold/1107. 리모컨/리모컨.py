import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

buttons = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

M = int(input())

err_buttons = set(map(int, input().split()))

work_buttons = buttons - err_buttons

K = list(map(int, str(N)))
length = len(K)

min_val = abs(100 - N)
min_num = 500001


def find_route(depth, set, N, lst):
    if depth == length + 1:
        global min_val, min_num
        a = int(''.join(lst))
        if abs(a - N) <= min_val:
            min_val = abs(a - N)
            min_num = a
        return

    for s in set:
        lst.append(str(s))
        find_route(depth + 1, set, N, lst)
        lst.pop()


find_route(0, work_buttons, N, [])

find_route(1, work_buttons, N, [])
if length != 1:
    find_route(2, work_buttons, N, [])

if N == 100:
    answer = 0
else:
    answer = min_val + len(list(str(min_num)))
    if abs(100 - N) < answer:
        answer = abs(100 - N)

# print(min_val)
# print(min_num)
print(answer)
