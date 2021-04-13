# 크로스워즈 만들기

a, b = map(str,input().split())
arr = [['.'] * len(a) for _ in range(len(b))]

tmp = list() # 겹치는 부분 찾기
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            tmp.append([i, j])

# 맨 앞은 tmp[0][0], tmp[0][1] = 1, 4
for i in range(len(a)):
    arr[tmp[0][1]][i] = a[i]

for j in range(len(b)):
    arr[j][tmp[0][0]] = b[j]

# 출력
for i in range(len(b)):
    print(''.join(arr[i]))
