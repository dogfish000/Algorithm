import sys
from collections import deque
input = sys.stdin.readline

def check_cycle(start):
    copy_dist = dist.copy()
    copy_dist[start] = 0

    for i in range(N):
        for item in edges:
            cur_node = item[0]
            next_node = item[1]
            cost = item[2]

            if copy_dist[cur_node] != 987654321 and copy_dist[next_node] > copy_dist[cur_node] + cost:
                copy_dist[next_node] = copy_dist[cur_node] + cost

                if i == N - 1:
                    return True

    return False


T = int(input())

for tc in range(1, T + 1):
    N, M, W = map(int, input().split())

    edges = []
    wormhole_lst = []

    for _ in range(M):
        s, e, k = map(int, input().split())
        edges.append([s, e, k])
        edges.append([e, s, k])

    for _ in range(W):
        s, e, k = map(int, input().split())
        edges.append([s, e, -k])
        wormhole_lst.append([s, e, k])

    dist = [987654321] * (N + 1)

    is_minus = 0
    for wormhole in wormhole_lst:
        start_node = wormhole[1]
        is_minus = check_cycle(start_node)

        if is_minus:
            break

    if is_minus:
        print("YES")
    else:
        print("NO")

