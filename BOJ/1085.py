# 직사각형에서 탈출

x, y, w, h = list(map(int, input().split()))

a = abs(h-y)
b = abs(w-x)

print(min(a,b,x,y))
