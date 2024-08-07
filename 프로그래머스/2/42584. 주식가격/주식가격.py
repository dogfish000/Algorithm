def solution(prices):
    len_prices = len(prices)
    answer = [0] * len_prices
    
    stack = []
    
    
    for i in range(len_prices):
        if not stack:
            stack.append([prices[i], i])
        else:
            while stack:
                if prices[i] >= stack[-1][0]:
                    break
                else:
                    a, b = stack.pop()
                    answer[b] = i - b
            
            stack.append([prices[i], i])
            
                    
        
    while stack:
        time = len_prices - 1
        a, b = stack.pop()
        answer[b] = time - b
    
    
    

    return answer