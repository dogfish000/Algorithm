def dfs(dic, visited, v):
    stack = [v]

    while stack:
        v = stack.pop()
        if v in dic:
            if visited[v] == 0:
                visited[v] = 1
                for w in dic[v]:
                    stack.append(w)


N = int(input())
M = int(input())

if N == 1:
    print(0)
else:

    lan_dic = {}
    
    visited = [0] * (N + 1)
    
    for _ in range(M):
        a, b = map(int, input().split())
    
        lan_dic[a] = lan_dic.get(a, []) + [b]
        lan_dic[b] = lan_dic.get(b, []) + [a]
    
    dfs(lan_dic, visited, 1)
    
    print(sum(visited) - 1)
