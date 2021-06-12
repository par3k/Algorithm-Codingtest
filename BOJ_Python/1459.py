# 걷기

x, y, w, s = map(int, input().split())
X, Y = min(x, y), max(x, y)
m = (X + Y) % 2
print(min((X + Y) * w, X * s + (Y - X) * w, (Y - m) * s + m * w))