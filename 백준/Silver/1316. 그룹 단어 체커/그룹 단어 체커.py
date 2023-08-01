N = int(input())
cnt_word = N


for _ in range(N):
    word = input()
    word_set = set(list(word))
    cnt = 1

    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            cnt += 1

    if cnt != len(word_set):
        cnt_word -= 1

print(cnt_word)
