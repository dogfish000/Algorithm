def solution(n, words):
    answer = []
    
    dsq = 0
    turn = 0
    stack = []
    
    for i in range(len(words)):
        if not stack:
            stack.append(words[i])
        else:
            if stack[-1][-1] != words[i][0]:
                dsq = i % n + 1
                turn = i // n + 1
                
                break
            if words[i] in stack:
                dsq = i % n + 1
                turn = i // n + 1
                
                break
            stack.append(words[i])
    answer = [dsq, turn]
    return answer