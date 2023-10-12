import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())

distance = [987654321] * (N + 1)

graph = [[] for i in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end] - distance[start])




