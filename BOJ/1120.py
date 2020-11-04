# 문자열

x, y = input().split()
y = list(y)

max_cnt = 0

while len(x) <= len(y):
    cnt = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            cnt += 1
    max_cnt = max(max_cnt, cnt)
    del y[0]
    
print(len(x) - max_cnt)