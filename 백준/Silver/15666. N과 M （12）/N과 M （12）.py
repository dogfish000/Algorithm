import sys
input = sys.stdin.readline

N, M = map(int, input().split())

answer = []

num_lst = list(map(int, input().split()))

def find_seq(depth, prev, lst):

    if depth == M:
        if lst not in answer:
            answer.append(lst)
        return

    for i in range(len(num_lst)):
        if num_lst[i] >= prev:
            find_seq(depth + 1, num_lst[i], lst + [num_lst[i]])


find_seq(0, 0, [])

answer.sort()

for item in answer:
    print(*item)