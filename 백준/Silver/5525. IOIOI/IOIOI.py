import sys

input = sys.stdin.readline

N = int(input())

M = int(input())

S = input().rstrip()

def oioi(N):
    res = 'I'

    for i in range(N):
        res += "OI"

    return res

cnt = 0
find_word = oioi(N)

while True:
    cnt += S.count(find_word)

    if not find_word in S:
        break


    S = S.replace(oioi(N), oioi(N - 1))





print(cnt)