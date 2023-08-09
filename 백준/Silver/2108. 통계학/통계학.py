import sys
input = sys.stdin.readline

N = int(input())

lst = []
cnt_lst = [0] * 8001

for _ in range(N):
    a = int(input())
    lst.append(a)
    cnt_lst[a + 4000] += 1

lst.sort()

print(round(sum(lst) / N))

print(lst[N // 2])

max_val = max(cnt_lst)

idx = cnt_lst.index(max_val)

if cnt_lst.count(max_val) >= 2:
    idx2 = cnt_lst.index(max_val, idx + 1)
    print(idx2 - 4000)
else:
    print(idx - 4000)

print(max(lst) - min(lst))

