import sys
input = sys.stdin.readline


N, M = map(int, input().split())

dic = {}

for _ in range(M):
    s, e = map(int, input().split())

    dic[s] = dic.get(s, []) + [e]
    dic[e] = dic.get(e, []) + [s]


def dfs(s, visited):
    stack = [s]

    while stack:
        v = stack.pop()
        if v not in visited and v in dic:
            visited.add(v)
            for w in dic[v]:
                stack.append(w)

    return visited


cnt = 0
visit = set()


for i in range(1, N + 1):
    if i not in visit:
        dfs(i, visit)
        cnt += 1


print(cnt)