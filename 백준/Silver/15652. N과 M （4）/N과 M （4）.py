import sys

input = sys.stdin.readline


N, M = map(int, input().split())


def find_seq(start_idx, lst, depth):
    if depth == M:
        print(*lst)
        return

    for i in range(start_idx, N + 1):
        lst.append(i)
        find_seq(i, lst, depth + 1)
        lst.remove(i)


find_seq(1, [], 0)






