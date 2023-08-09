import sys
import math

input = sys.stdin.readline

N, M, B = map(int, input().split())

minecraft = []

for _ in range(N):
    minecraft.append(list(map(int, input().split())))

max_val = 0
min_val = 256

for item in minecraft:
    max_val = max(max_val, max(item))
    min_val = min(min_val, min(item))

time_record = 500 * 500 * 256 * 3
height_record = 257

for h in range(max_val, min_val - 1, -1):
    time = 0
    block = B
    for i in range(N):
        for j in range(M):
            diff = minecraft[i][j] - h
            if diff > 0:
                time += 2 * diff
                block += diff
            else:
                time -= diff
                block += diff

    if time < time_record and block >= 0:
        time_record = time
        height_record = h

print(time_record, height_record)
