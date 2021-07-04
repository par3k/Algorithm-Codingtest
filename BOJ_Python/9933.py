# 민균이의 비밀번호
import sys
input = lambda :sys.stdin.readline().rstrip()

arr = []
for _ in range(int(input())):
    arr.append(input())


def pelin(cha):
    res = ''
    for i in range(len(cha)-1, -1, -1):
        res += cha[i]
    return res


tmp = []
for i in range(len(arr)):
    tmp.append(pelin(arr[i]))

ans = ''
for i in range(len(arr)):
    for j in range(i, len(tmp)):
        if tmp[j] == arr[i]:
            ans = tmp[j]

print(len(ans), end=' ')
print(ans[(len(ans) -1) // 2])