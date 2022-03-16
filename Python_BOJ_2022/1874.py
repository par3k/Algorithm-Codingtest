# 스택 수열
cnt = 1
tmp = []
ans = []
flag = True

for _ in range(int(input())):
    n = int(input())
    while cnt <= n:
        tmp.append(cnt)
        ans.append('+')
        cnt += 1

    if tmp[-1] == n:
        tmp.pop()
        ans.append('-')
    else:
        flag = False

if not flag:
    print("NO")
else:
    for i in ans:
        print(i)