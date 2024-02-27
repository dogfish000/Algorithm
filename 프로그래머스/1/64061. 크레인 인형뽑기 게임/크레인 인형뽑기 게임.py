def solution(board, moves):
    answer = 0
    
    lst = []
    
    for mv in moves:
        for i in range(len(board)):
            if board[i][mv - 1] != 0:
                lst.append(board[i][mv-1])
                board[i][mv-1] = 0
                break
        
        if len(lst) >= 2 and lst[-1] == lst[-2]:
            for _ in range(2):
                lst.pop()
                answer += 1
            
    
    
    return answer