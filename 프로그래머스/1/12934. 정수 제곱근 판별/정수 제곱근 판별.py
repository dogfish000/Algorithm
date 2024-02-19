def solution(n):
    answer = -1
    root = int(n ** (1/2))
    print(root)
    
    for i in range(1, root + 1):
        if (i ** 2 == n):
            answer = (i + 1) ** 2
    
    return answer