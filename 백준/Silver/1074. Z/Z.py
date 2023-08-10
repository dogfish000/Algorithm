N, r, c = map(int, input().split())

start = 0
end = 0
c_left = 0
c_right = 2 ** N - 1
r_left = 0
r_right = 2 ** N - 1

for i in range(N, 0, -1):
    r_mid = (r_left + r_right) // 2
    c_mid = (c_left + c_right) // 2
    if r <= r_mid and c <= c_mid:
        quad = 0
        r_right = r_mid
        c_right = c_mid

    elif r <= r_mid and c > c_mid:
        quad = 1
        r_right = r_mid
        c_left = c_mid + 1

    elif r > r_mid and c <= c_mid:
        quad = 2
        r_left = r_mid + 1
        c_right = c_mid

    elif r > r_mid and c > c_mid:
        quad = 3
        r_left = r_mid + 1
        c_left = c_mid + 1

    num = (2 ** (i - 1)) ** 2
    start = start + quad * num
    end = start - 1 + num

print(end)

