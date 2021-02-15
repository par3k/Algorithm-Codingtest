# 네 번째 점

x = []
y = []

for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

if x.count(x[2]) == 1:
    print(x[2], end='')
elif x.count(x[0]) == 1:
    print(x[0], end='')

if y.count(y[2]) == 1:
    print("", y[2])
elif y.count(y[0]) == 1:
    print("", y[0])