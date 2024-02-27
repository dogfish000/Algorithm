def solution(dartResult):
    answer = []
    
    tmp = ''
    for d in dartResult:
        if d.isdigit():
            tmp += d
        elif d == 'S':
            answer.append(int(tmp))
            tmp = ''
        elif d == 'D':
            answer.append(int(tmp) ** 2)
            tmp = ''
        elif d == 'T':
            answer.append(int(tmp) ** 3)
            tmp = ''
        elif d == '*':
            if len(answer) >= 2:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * 2
        elif d == '#':
            answer[-1] = -answer[-1]
            
    return sum(answer)