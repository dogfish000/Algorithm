import sys
input = sys.stdin.readline


N = int(input())

graph = []
visited = []
dic = {}

for _ in range(N):
    graph.append(list(map(int, input().split())))
    visited.append([0] * N)

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dic[i] = dic.get(i, []) + [j]


def dfs(start, end):
    stack = [start]
    visit = []

    while stack:
        v = stack.pop()
        if v in dic:
            for w in dic[v]:
                if w not in visit:
                    visit.append(w)
                    stack.append(w)

    if end in visit:
        return 1
    else:
        return 0


for i in range(N):
    for j in range(N):
        visited[i][j] = dfs(i, j)


for i in range(N):
    print(*visited[i], sep=' ')