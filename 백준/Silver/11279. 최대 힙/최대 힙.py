import sys
import heapq

input = sys.stdin.readline

N = int(input())


heap = []

for _ in range(N):
    a = int(input())

    if a == 0:
        if len(heap) == 0:
            print(0)
        else:
            num = heapq.heappop(heap)
            print(-num)

    else:
        heapq.heappush(heap, -a)
