def solution(name, yearning, photo):
    answer = []
    
    for ns in photo:
        tmp = 0
        for n in ns:
            if n in name:
                tmp += yearning[name.index(n)]
        answer.append(tmp)
    
    return answer