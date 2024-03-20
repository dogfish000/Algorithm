def solution(want, number, discount):
    answer = 0
    
    for i in range(0, len(discount) - 9):
        tmp = discount[i: i + 10]
        tmp_bool = True
        for j in range(len(want)):
            if tmp.count(want[j]) < number[j]:
                tmp_bool = False
        if tmp_bool:
            answer += 1
    
    
    
    return answer