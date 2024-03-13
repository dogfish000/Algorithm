def solution(s):

    stack = []
    
    for st in s:
        if not stack:
            stack.append(st)
        else:
            if st == stack[-1]:
                stack.pop()
            else:
                stack.append(st)
        
    if stack:
        return 0
    
    else:
        return 1
    
