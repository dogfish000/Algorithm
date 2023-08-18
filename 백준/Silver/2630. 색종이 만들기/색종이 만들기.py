import sys

input = sys.stdin.readline

N = int(input())

paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

cnt_w = 0
cnt_b = 0

def cut_paper(row_l, row_r, col_l, col_r):
    global cnt_w, cnt_b
    width = col_r - col_l + 1

    if col_r == col_l:
        a = paper[row_l][col_l]
        if a == 0:
            cnt_w += 1
        else:
            cnt_b += 1
        return
    
    tmp = 0
    for i in range(row_l, row_r + 1):
        for j in range(col_l, col_r + 1):
            tmp += paper[i][j]

    if tmp == 0:
        cnt_w += 1
    elif tmp == width ** 2:
        cnt_b += 1
    else:
        row_mid = (row_l + row_r) // 2
        col_mid = (col_l + col_r) // 2
        cut_paper(row_l, row_mid, col_l, col_mid)
        cut_paper(row_l, row_mid, col_mid + 1, col_r)
        cut_paper(row_mid + 1, row_r, col_l, col_mid)
        cut_paper(row_mid + 1, row_r, col_mid + 1, col_r)


cut_paper(0, N - 1, 0, N - 1)

print(cnt_w)
print(cnt_b)


