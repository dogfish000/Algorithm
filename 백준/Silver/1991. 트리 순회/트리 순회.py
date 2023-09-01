import sys
input = sys.stdin.readline

N = int(input())

graph = {}

for _ in range(N):
    a, b, c = input().split()

    graph[a] = graph.get(a, []) + [b, c]

# print(graph)


def pre(start):

    tmp = graph[start]

    pre_lst.append(start)

    if tmp[0] != '.':
        pre(tmp[0])

    if tmp[1] != '.':
        pre(tmp[1])


def mid(start):
    tmp = graph[start]

    if tmp[0] != '.':
        mid(tmp[0])

    mid_lst.append(start)

    if tmp[1] != '.':
        mid(tmp[1])


def post(start):
    tmp = graph[start]

    if tmp[0] != '.':
        post(tmp[0])

    if tmp[1] != '.':
        post(tmp[1])

    post_lst.append(start)

start_idx = 'A'

pre_lst = []
mid_lst = []
post_lst = []


pre(start_idx)
mid(start_idx)
post(start_idx)

print(*pre_lst, sep='')
print(*mid_lst, sep='')
print(*post_lst, sep='')

