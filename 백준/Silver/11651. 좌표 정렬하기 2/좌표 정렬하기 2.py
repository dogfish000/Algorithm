import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    stack.append(list(map(int, input().split())))


stack.sort(key=lambda x: (x[1], x[0]))

for i in range(len(stack)):
    print(*stack[i])
