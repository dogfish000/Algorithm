import sys
import heapq
input = sys.stdin.readline


N = int(input())

heap = []

for _ in range(N):
    a = int(input())

    if a == 0:
        if not len(heap) == 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        heapq.heappush(heap, (abs(a), a))



