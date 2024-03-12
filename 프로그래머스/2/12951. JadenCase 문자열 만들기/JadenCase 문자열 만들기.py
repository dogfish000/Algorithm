def solution(s):
    answer = []
    
    lst = list(s.split(" "))
    
    for l in lst:
        l = l.capitalize()
        answer.append(l)
    
    return ' '.join(answer)