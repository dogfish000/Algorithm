import sys
input = sys.stdin.readline



N, M = map(int, input().split())

no_hear = set()

no_look = set()

for _ in range(N):
    no_hear.add(sys.stdin.readline().rstrip())

for _ in range(M):
    no_look.add(sys.stdin.readline().rstrip())


no_hear_look = no_hear & no_look

no_hear_look = list(no_hear_look)
no_hear_look.sort()
K = len(no_hear_look)

print(K)
for i in range(K):
    print(no_hear_look[i])