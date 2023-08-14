import sys
input = sys.stdin.readline


N, M = map(int, input().split())

tree_lst = list(map(int, input().split()))

start = 0
end = max(tree_lst)

def binary_search(start, lst, K):
    s = start
    e = max(lst)

    while s <= e:
        mid = (s + e) // 2

        tmp = 0
        for item in lst:
            if item > mid:
                tmp += (item - mid)

        if tmp == K:
            return mid

        elif tmp > K:
            s = mid + 1

        else:
            e = mid - 1

    return e


a = binary_search(start, tree_lst, M)
print(a)