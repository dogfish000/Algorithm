def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    
    
    
    numbers.sort(key= lambda x: x*3)
    numbers.reverse()
    
    for num in numbers:
        answer += num
    
    answer = int(answer)
    answer = str(answer)
    
    
    return answer