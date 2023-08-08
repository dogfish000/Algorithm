import sys

input = sys.stdin.readline


N = int(input())

push_pop_lst = []
stack = []

cur = 1
is_possible = 1

for _ in range(N):
    input_val = int(input())

    while cur <= input_val:
        stack.append(cur)
        push_pop_lst.append('+')
        cur += 1

    if stack[-1] == input_val:
        stack.pop()
        push_pop_lst.append('-')
    else:
        is_possible = 0
        print("NO")
        break

if is_possible:
    for item in push_pop_lst:
        print(item)
