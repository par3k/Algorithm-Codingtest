# 수강신청
import sys
input = sys.stdin.readline

k, l = map(int, input().split())
tmp = dict()

for i in range(l):
    stu = int(input().rsplit())
    tmp[stu] = i

tmp = sorted(tmp.items(), key=lambda x: x[1])

if k > len(tmp):
    k = len(tmp)

for i in range(k):
    print(tmp[i][0])