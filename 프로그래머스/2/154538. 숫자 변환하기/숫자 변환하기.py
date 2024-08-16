from collections import deque

def solution(x, y, n):
    # 최솟값을 구할 때 가능한 큰 수로 초기화
    answer = -1
    
    # BFS를 위한 큐 초기화, (현재 깊이, 현재 숫자) 쌍을 저장
    queue = deque([(0, y)])
    
    # 방문 여부를 기록하기 위한 집합
    visited = set()
    visited.add(y)
    
    while queue:
        depth, num = queue.popleft()
        
        # 목표 숫자에 도달했을 경우, 최소 깊이를 반환
        if num == x:
            answer = depth
            break
        
        # 다음 단계에서 갈 수 있는 모든 경우의 수를 큐에 추가
        # 이때 이미 방문한 숫자는 다시 방문하지 않도록 체크
        if num % 2 == 0 and num // 2 not in visited:
            queue.append((depth + 1, num // 2))
            visited.add(num // 2)
        
        if num % 3 == 0 and num // 3 not in visited:
            queue.append((depth + 1, num // 3))
            visited.add(num // 3)
        
        if num - n >= x and (num - n) not in visited:
            queue.append((depth + 1, num - n))
            visited.add(num - n)
    
    return answer
