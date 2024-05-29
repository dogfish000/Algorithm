from collections import deque

def solution(maps):
    answer = 0
    N = len(maps) 
    M = len(maps[0])

    bfs(0, 0, maps)
    print(maps)
    
    answer = maps[N - 1][M - 1] if maps[N - 1][M - 1] != 1 else -1
    
    return answer


def bfs(start_i, start_j, maps):
    N = len(maps) 
    M = len(maps[0])
    dq = deque()
    dq.append([start_i, start_j])
    
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while dq:
        tmp = dq.popleft()
        i, j = tmp[0], tmp[1]
        for di, dj in dir:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and maps[ni][nj] == 1:
                dq.append([ni, nj])
                maps[ni][nj] = maps[i][j] + 1
    