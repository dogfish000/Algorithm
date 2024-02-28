def solution(wallpaper):
    answer = []
    
    min_i = 987654321
    max_i = -1
    min_j = 987654321
    max_j = -1
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            tmp = wallpaper[i][j]
            if tmp == '#':
                if i > max_i:
                    max_i = i
                if i < min_i:
                    min_i = i
                if j > max_j:
                    max_j = j
                if j < min_j:
                    min_j = j
    
    answer = [min_i, min_j, max_i + 1, max_j + 1]
    
    
    
    return answer