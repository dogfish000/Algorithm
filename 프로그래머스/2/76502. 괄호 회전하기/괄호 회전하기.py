def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += check_bracket(s)
        s = s[1:] + s[0]
    return answer



def check_bracket(s):
    a = []
    
    
    for i in range(len(s)):
        if s[i] == '[':
            a.append('[')
        elif s[i] == ']':
            if a and a[-1] == '[':
                a.pop()
            else:
                return 0
        if s[i] == '(':
            a.append('(')
        elif s[i] == ')':
            if a and a[-1] == '(':
                a.pop()
            else:
                return 0
        if s[i] == '{':
            a.append('{')
        elif s[i] == '}':
            if a and a[-1] == '{':
                a.pop()
            else:
                return 0
        
    if a:
        return 0
    else:
        return 1