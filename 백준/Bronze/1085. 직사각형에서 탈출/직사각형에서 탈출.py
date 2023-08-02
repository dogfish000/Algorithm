x, y, w, h = map(int, input().split())

route_x = min(x, w - x)
route_y = min(y, h - y)

print(min(route_x, route_y))

