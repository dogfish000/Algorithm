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

    for i in range(len(input_lst)):
        if depth == 0:
            a = input_lst[i]
            output_lst.append(a)
            dfs(output_lst, input_lst, depth + 1)
            output_lst.pop()
            
        else:
            a = input_lst[i]
            if a >= output_lst[-1]:
                output_lst.append(a)
                dfs(output_lst, input_lst, depth + 1)
                output_lst.pop()





dfs([], lst, 0)

subset_lst.sort()

for item in subset_lst:
    print(*item)
