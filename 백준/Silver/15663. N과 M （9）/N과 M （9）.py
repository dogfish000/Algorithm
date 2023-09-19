import sys
input = sys.stdin.readline

N, M = map(int, input().split())

seq_set = set()

lst = list(map(int, input().split()))

visited = [0] * N
def find_seq(input_lst, visited, depth):
    # 종료
    if depth == M:
        seq_set.add(tuple(input_lst))
        return

    # 실행
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            input_lst.append(lst[i])
            find_seq(input_lst, visited, depth + 1)
            input_lst.pop()
            visited[i] = 0

find_seq([], visited, 0)

seq_lst = list(seq_set)

seq_lst.sort()

for item in seq_lst:
    print(*item)