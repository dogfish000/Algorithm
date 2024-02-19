def solution(phone_number):
    answer = ''
    
    answer= '*' * (len(phone_number) - 4)
    answer = answer + phone_number[-4:]
    print(answer)
    
    return answer