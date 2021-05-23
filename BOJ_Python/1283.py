# 단축키 지정
import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().rstrip()

ans = []
dic = defaultdict(int)

for _ in range(int(input())):
    s = input().split()
    tmp = []
    cnt = 0
    flag = False

    for i in s:
        if flag:
            tmp.append(i)
            continue

        if i[0].upper() in dic:
            cnt += 1
            tmp.append(i)
        elif i[0].upper() not in dic and not flag:
            tmp.append(i.replace(i[0], '[' + i[0] + ']', 1))
            print(tmp)
            dic[i[0].upper()] += 1
            flag = True
            print(dic)

    if cnt == len(s):
        tmp = []
        for i in s:
            cnt = 0
            if flag:
                tmp.append(i)
                continue

            for j in i:
                if j.upper() in dic:
                    cnt += 1
                    if cnt == len(i):
                        tmp.append(i)
                elif not flag and j.upper() not in dic:
                    flag = True
                    dic[j.upper()] += 1
                    tmp.append(i.replace(j, '[' + j + ']', 1))
                    continue

    ans.append(' '.join(tmp))
for i in ans:
    print(i)
