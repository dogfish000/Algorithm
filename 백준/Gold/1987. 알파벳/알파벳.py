import sys

input = sys.stdin.readline

R, C = map(int, input().split())

lst = []

for _ in range(R):
    lst.append(list(input().rstrip()))


deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

visited = [0] * 26
answer = 0

def dfs(now_i, now_j, visited, depth):
    global answer

    if depth > answer:
        answer = depth

    for di, dj in deltas:
        ni, nj = now_i + di, now_j + dj
        if 0 <= ni < R and 0 <= nj < C:
            idx = ord(lst[ni][nj]) - ord('A')
            if visited[idx] == 0:
                visited[idx] = 1
                dfs(ni, nj, visited, depth + 1)
                visited[idx] = 0


start_idx = ord(lst[0][0]) - ord('A')

visited[start_idx] = 1


dfs(0, 0, visited, 1)


print(answer)




