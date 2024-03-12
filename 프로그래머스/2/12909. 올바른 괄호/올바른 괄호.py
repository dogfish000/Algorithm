def solution(s):
    answer = True
    
    stack_lst = []
    
    lst = list(s)
    
    for l in lst:
        if l == '(':
            stack_lst.append(1)
        else:
            if len(stack_lst) == 0:
                answer = False
                break
            else:
                stack_lst.pop()
    
    if stack_lst:
        answer = False

    return answer