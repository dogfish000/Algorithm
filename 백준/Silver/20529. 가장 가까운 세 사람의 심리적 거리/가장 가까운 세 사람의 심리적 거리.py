import sys
input = sys.stdin.readline

def find_min(start_idx, depth, s_lst, tmp_lst, visited):
    # global
    global min_val

    # 종료 조건
    if depth == 3:
        cnt = 0
        for i in range(4):
            if tmp_lst[0][i] != tmp_lst[1][i]:
                cnt += 1
            if tmp_lst[1][i] != tmp_lst[2][i]:
                cnt += 1
            if tmp_lst[2][i] != tmp_lst[0][i]:
                cnt += 1
        min_val = min(min_val, cnt)
        return

    # 실행문
    for i in range(start_idx, len(s_lst)):
        if i not in visited:
            tmp_lst.append(s_lst[i])
            visited.append(i)
            find_min(i, depth + 1, s_lst, tmp_lst, visited)
            tmp_lst.remove(s_lst[i])
            visited.remove(i)



T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    answer = 0
    lst = input().split()
    if N <= 32:

        dic = {}

        for item in lst:
            dic[item] = dic.get(item, 0) + 1

        is_three = 0
        for item in dic.values():
            if item >= 3:
                answer = 0
                is_three = 1
                break

        if not is_three:
            min_val = 12
            find_min(0, 0, lst, [], [])
            answer = min_val

    print(answer)








