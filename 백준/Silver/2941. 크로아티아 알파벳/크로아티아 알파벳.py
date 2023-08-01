S = input()
cnt = 0

for i in range(len(S)):
    cnt += 1
    if S[i] == '=':
        if S[i - 1] in ['c', 'z', 's']:
            cnt -= 1
            if S[i - 1] == 'z':
                if S[i - 2] == 'd':
                    cnt -= 1

    if S[i] == '-':
        if S[i - 1] in ['c', 'd']:
            cnt -= 1

    if S[i] == 'j':
        if S[i - 1] in ['l', 'n']:
            cnt -= 1


print(cnt)
