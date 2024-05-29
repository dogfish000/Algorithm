def solution(numbers, target):
    global answer
    answer = 0
    max_idx = len(numbers)
    
    
    def target_number(num, idx):
        global answer
        if idx == max_idx:
            if num == target:
                answer += 1
            return
    
        target_number(num + numbers[idx], idx + 1)
        target_number(num - numbers[idx], idx + 1)
        
    
    target_number(0, 0)
    
    
    
    
    
    
    return answer