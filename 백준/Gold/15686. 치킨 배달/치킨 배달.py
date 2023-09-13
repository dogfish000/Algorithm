import sys
import copy
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]


chicken_lst = []
house_lst = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken_lst.append([i, j])
        elif city[i][j] == 1:
            house_lst.append([i, j])

# print(chicken_lst)
# print(house_lst)


nums = []

for i in range(0, len(chicken_lst)):
    nums.append(i)

subsets = []
n = len(nums)

for i in range(1 << n):
    subset = []
    for j in range(n):
        if (i >> j) & 1:
            subset.append(nums[j])

    if len(subset) == M:
        subsets.append(subset)

# print(subsets)


route_lst = []

for house in house_lst:
    house_x, house_y = house[0], house[1]
    tmp_lst = []
    for chicken in chicken_lst:
        chicken_x, chicken_y = chicken[0], chicken[1]
        tmp_val = abs(house_x - chicken_x) + abs(house_y - chicken_y)
        tmp_lst.append(tmp_val)

    route_lst.append(tmp_lst)

min_val = 99999999

for items in subsets:
    tmp_val = 0
    for route in route_lst:
        tmp_min = 99999999
        for item in items:
            tmp_min = min(tmp_min, route[item])
        tmp_val += tmp_min

    min_val = min(min_val, tmp_val)

print(min_val)



