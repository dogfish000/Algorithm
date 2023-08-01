S = input()
cnt_lst = []

for idx in range(ord('a'), ord('z') + 1):
    tmp = S.find(chr(idx))
    cnt_lst.append(tmp)

print(*cnt_lst)
