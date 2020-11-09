# 오타맨 고창영
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    ans = list()
    a = list(map(str, input().split()))
    for i in range(len(a[1])):
        if i == int(a[0]) - 1:
            pass
        else:
            ans.append(a[1][i])

    print(''.join(ans))