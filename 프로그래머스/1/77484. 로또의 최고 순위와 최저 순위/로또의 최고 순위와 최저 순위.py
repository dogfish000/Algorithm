def solution(lottos, win_nums):
    answer = []
    
    cnt = 0
    
    for num in win_nums:
        if num in lottos:
            cnt += 1
            
    min_cnt = cnt
    max_cnt = min(cnt + lottos.count(0), 6)
    
    min_rank = 7 - min_cnt if min_cnt >= 2 else 6
    max_rank = 7 - max_cnt if max_cnt >= 2 else 6
    
    answer = [max_rank, min_rank]
    
    
    return answer