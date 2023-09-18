import sys
input = sys.stdin.readline


N, M = map(int, input().split())

lst = list(map(int, input().split()))

# print(lst)


subset_lst = []

n = len(lst)

def dfs(output_lst, input_lst, depth):

    if depth == M:
        subset_lst.append(output_lst.copy())
        return

    for _ in range(len(input_lst)):
        a = input_lst.pop(0)
        output_lst.append(a)
        dfs(output_lst, input_lst, depth + 1)
        output_lst.pop()
        input_lst.append(a)


dfs([], lst, 0)

subset_lst.sort()

for item in subset_lst:
    print(*item)
