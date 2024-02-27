def solution(board, h, w):
    answer = 0
    n = len(board)
    
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dh, dw in dir:
        nh, nw = h + dh, w + dw
        if 0 <= nh < n and 0 <= nw < n and board[nh][nw] == board[h][w]:
            answer += 1
    
    
    
    return answer