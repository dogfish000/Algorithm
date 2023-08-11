import sys

N, M = map(int, sys.stdin.readline().split())

pass_dic = {}

for _ in range(N):
    site, pw = sys.stdin.readline().rstrip().split()

    pass_dic[site] = pw

for _ in range(M):
    a = sys.stdin.readline().rstrip()

    print(pass_dic[a])
