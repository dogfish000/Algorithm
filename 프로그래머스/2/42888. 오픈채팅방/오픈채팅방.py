def solution(record):
    
    answer = []
    # uid, 입장 퇴장
    lst = []
    
    # uid와 닉네임 매치
    dic = {}
    
    # 나가면 0 들어오면 1
    for r in record:
        a = r.split()
        if len(a) == 2:
            lst.append([0, a[1]])
        else:
            if a[0] == 'Change':
                dic[a[1]] = a[2]
            else:
                dic[a[1]] = a[2]
                lst.append([1, a[1]])
    
    for l in lst:
        if l[0] == 0:
            answer.append(f'{dic[l[1]]}님이 나갔습니다.')
        else:
            answer.append(f'{dic[l[1]]}님이 들어왔습니다.')
            
            
            
    
    
    return answer