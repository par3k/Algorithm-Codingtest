# 창고 다각형
import sys
input = lambda :sys.stdin.readline().rstrip()

max_L, max_H, max_Idx = 0, 1, 0
arr = list()

for i in range(int(input())):
    idx, height = map(int, input().split())
    arr.append([idx, height])

    if max_L < idx: # 가장 마지막 idx
        max_L = idx

    if max_H < height: # 가장 높은것
        max_H = height # 높이
        max_Idx = idx # 높은 녀석의 idx

list = [0] * (max_L + 1)
for i, h in arr:
    list[i] = h

tmp, ans = 0, 0
for i in range(max_Idx + 1):
    if list[i] > tmp:
        tmp = list[i]
    ans += tmp

tmp = 0
for i in range(max_L, max_Idx, -1):
    if list[i] > tmp:
        tmp = list[i]
    ans += tmp

print(ans)