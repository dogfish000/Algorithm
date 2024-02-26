def solution(babbling):
    answer = 0
    
    for b in babbling:
        if chk_bab(b):
            answer += 1
    
    return answer


def chk_bab(w):
    w = w.replace('ayaaya', 'k')
    w = w.replace('yeye', 'k')
    w = w.replace('woowoo', 'k')
    w = w.replace('mama', 'k')
    
    w = w.replace('aya', '1')
    w = w.replace('ye', '1')
    w = w.replace('woo', '1')
    w = w.replace('ma', '1')
    w = w.replace('1', '')
    
    if w == '':
        return True
    else:
        return False