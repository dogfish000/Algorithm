import sys

N, M = map(int, input().split())

poke_dic = {}

for i in range(1, N + 1):
    poke_name = sys.stdin.readline().rstrip()
    poke_dic[str(i)] = poke_name
    poke_dic[poke_name] = str(i)


for _ in range(M):
    a = sys.stdin.readline().rstrip()
    print(poke_dic[a])