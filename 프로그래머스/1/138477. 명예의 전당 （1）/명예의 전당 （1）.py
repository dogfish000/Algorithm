def solution(k, score):
    answer = []
    
    hof = []
    
    for s in score:
        hof.append(s)
        hof.sort()
        if len(hof) > k:
            hof = hof[1:]
        answer.append(hof[0])
    
    
    return answer