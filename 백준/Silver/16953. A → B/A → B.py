import sys
input = sys.stdin.readline

A, B = map(int, input().split())

lst = [(A, 1)]

answer = 987654321

while lst:
    num, cnt = lst.pop(0)
    if num == B:
        answer = min(cnt, answer)
        continue
    if num * 2 <= B:
        lst.append((num * 2, cnt + 1))
    if num * 10 + 1 <= B:
        lst.append((num * 10 + 1, cnt + 1))

if answer != 987654321:
    print(answer)
else:
    print(-1)

