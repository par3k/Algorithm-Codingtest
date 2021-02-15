# 비밀편지
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
s = list(str(input()))
ans = []
err_cnt = 0

word = [['0', '0', '0', '0', '0', '0'],  # A
        ['0', '0', '1', '1', '1', '1'],  # B
        ['0', '1', '0', '0', '1', '1'],  # C
        ['0', '1', '1', '1', '0', '0'],  # D
        ['1', '0', '0', '1', '1', '0'],  # E
        ['1', '0', '1', '0', '0', '1'],  # F
        ['1', '1', '0', '1', '0', '1'],  # G
        ['1', '1', '1', '0', '1', '0']]  # H
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def modify(arr):
    k = list()
    for i in range(8):
        chk = 0
        for j in range(6):
            if arr[j] != word[i][j]:
                chk += 1
        k.append([chk, i])
        k.sort()
    if k[0][0] == 1:
        return k[0][1]
    else:
        return -1


for i in range(n):
    flag = False
    for j in range(8):
        if s[0:6] == word[j]:
            ans.append(alpha[j])
            flag = True
        else:
            pass

    if not flag:
        if modify(s[0:6]) == -1:
            err_cnt = 1
            m = i + 1
            break
        else:
            ans.append(alpha[modify(s[0:6])])
    del s[0:6]
    if err_cnt == 1:
        break

if err_cnt == 1:
    print(m)
else:
    for i in range(n):
        print(ans[i], end='')

