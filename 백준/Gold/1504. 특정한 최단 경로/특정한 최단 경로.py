import sys
input = sys.stdin.readline
import heapq

INF = 987654321

N, M = map(int, input().split())

graph = [[] for i in range(N + 1)]

lst = []

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def find(start, end):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            next_dist = dist + i[1]
            if next_dist < distance[i[0]]:
                distance[i[0]] = next_dist
                heapq.heappush(q, (next_dist, i[0]))

    if distance[end] == INF:
        return -987654321
    else:
        return distance[end] - distance[start]


v1, v2 = map(int, input().split())

dist_v1 = find(1, v1) + find(v1, v2) + find(v2, N)
dist_v2 = find(1, v2) + find(v2, v1) + find(v1, N)

if dist_v1 > 0:
    if dist_v2 > 0:
        answer = min(dist_v1, dist_v2)
    else:
        answer = dist_v1

else:
    if dist_v2 > 0:
        answer = dist_v2
    else:
        answer = -1


print(answer)