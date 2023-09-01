import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

INF = int(1e9)

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


dist = [INF] * (V + 1)

dist[K] = 0

queue = []

def find_min_path (start):
    heapq.heappush(queue, (0, start))

    while queue:
        tmp_dist, cur = heapq.heappop(queue)

        if tmp_dist > dist[cur]:
            continue
        for item in graph[cur]:
            d, nxt = item[1], item[0]
            cost = d + tmp_dist
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(queue, (cost, nxt))



find_min_path(K)

for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])