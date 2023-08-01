S = input()

S = S.lower()

# 'a' => 97

cnt_lst = [0] * 26

for s in S:
    idx = ord(s) - ord('a')
    cnt_lst[idx] += 1

max_value = -1

for cnt in cnt_lst:
    if cnt >= max_value:
        max_value = cnt

if cnt_lst.count(max_value) >= 2:
    print("?")
else:
    print(chr(cnt_lst.index(max_value) + ord('A')))


