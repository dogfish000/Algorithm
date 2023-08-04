def check_board(row, col, board):
    cnt_1 = 0
    for p in range(row, row + 8):
        for q in range(col, col + 8):
            if (p + q) % 2 == 0:
                if board[p][q] != 'B':
                    cnt_1 += 1
            else:
                if board[p][q] != 'W':
                    cnt_1 += 1

    cnt_2 = 0
    for p in range(row, row + 8):
        for q in range(col, col + 8):
            if (p + q) % 2 == 0:
                if board[p][q] != 'W':
                    cnt_2 += 1
            else:
                if board[p][q] != 'B':
                    cnt_2 += 1

    return min(cnt_1, cnt_2)


N, M = map(int, input().split())

chess_board = []

for _ in range(N):
    chess_board.append(list(input()))

min_val = N * M

for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        val = check_board(i, j, chess_board)
        min_val = min(min_val, val)

print(min_val)
