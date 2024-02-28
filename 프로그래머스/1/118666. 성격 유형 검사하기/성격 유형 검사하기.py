def solution(survey, choices):
    answer = ''
    
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        choice = choices[i] - 4
        print(survey[i][0])
        if choice < 0:
            dic[survey[i][0]] += abs(choice)
        elif choice > 0:
            dic[survey[i][1]] += abs(choice)
    
    if dic['T'] > dic['R']:
        answer += 'T'
    else:
        answer += 'R'
    
    
    if dic['F'] > dic['C']:
        answer += 'F'
    else:
        answer += 'C'
        
    if dic['M'] > dic['J']:
        answer += 'M'
    else:
        answer += 'J'
        
    if dic['N'] > dic['A']:
        answer += 'N'
    else:
        answer += 'A'
    
    return answer