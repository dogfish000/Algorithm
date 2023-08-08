import sys

input = sys.stdin.readline


def binary_search(arr, key):
    start = 1
    end = 2 ** 31 - 1
    middle = 0

    while start <= end:
        middle = (start + end) // 2

        sum_val = 0
        for a in arr:
            sum_val += a // middle

        if sum_val >= key:
            start = middle + 1

        else:
            end = middle - 1

    return end


N, K = map(int, input().split())

cables = []
for _ in range(N):
    cables.append(int(input()))

div = binary_search(cables, K)

print(div)

