from collections import deque

N, M, V = map(int, input().split())

dic = {}

for _ in range(M):
    s, e = map(int, input().split())

    dic[s] = dic.get(s, []) + [e]
    dic[e] = dic.get(e, []) + [s]


def dfs(start):
    stack = [start]
    visited = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v in dic:
                tmp = []
                for w in dic[v]:
                    tmp.append(w)
                tmp.sort()
                while tmp:
                    stack.append(tmp.pop())

    return visited


def bfs(start):
    queue = deque([start])
    visited = []

    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            if v in dic:
                tmp = []
                for w in dic[v]:
                    tmp.append(w)
                tmp.sort()
                queue.extend(tmp)

    return visited


a = dfs(V)
b = bfs(V)

print(*a, sep=' ')
print(*b, sep=' ')