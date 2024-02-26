def solution(answers):
    answer = []
    
    math_1 = [1, 2, 3, 4, 5]
    math_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    math_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == math_1[i % 5]:
            cnt_1 += 1
        if answers[i] == math_2[i % 8]:
            cnt_2 += 1
        if answers[i] == math_3[i % 10]:
            cnt_3 += 1
    
    print(cnt_1, cnt_2, cnt_3)
    max_cnt = max(cnt_1, cnt_2, cnt_3)
    
    if cnt_1 == max_cnt:
        answer.append(1)
    if cnt_2 == max_cnt:
        answer.append(2)
    if cnt_3 == max_cnt:
        answer.append(3)
        
    
    
    return answer