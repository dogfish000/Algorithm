T = int(input())

for tc in range(1, T + 1):
    H, W, N = map(int, input().split())

    room = (100 * (1 + ((N - 1) % H))) + (1 + ((N - 1) // H))

    print(room)