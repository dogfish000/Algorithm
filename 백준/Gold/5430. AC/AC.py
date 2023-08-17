import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    p = input().rstrip()
    n = int(input())
    word = input().rstrip()
    word2 = word[1: len(word) - 1]
    if word2 == '':
        lst = []
    else:
        lst = list(map(int, word2.split(',')))

    queue = deque(lst)


    is_flag = 0
    is_reverse = 0
    for item in p:
        if item == 'R':
            is_reverse = (is_reverse + 1) % 2
        if item == 'D':
            if len(queue) == 0:
                is_flag = 1
                break
            else:
                if is_reverse:
                    queue.pop()
                else:
                    queue.popleft()

    lst = list(queue)



    if is_flag:
        print("error")
    else:
        if is_reverse:
            lst.reverse()
        print("[", end='')
        print(*lst, sep=',', end='')
        print("]")


