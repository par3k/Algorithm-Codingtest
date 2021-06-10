# 저항
import sys
input = lambda :sys.stdin.readline().rstrip()

arr = []
regist = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
for _ in range(3):
    s = input()
    arr.append(s)

tmp = ''
tmp2 = 0

for i in range(2):
    for j in range(len(regist)):
        if regist[j] == arr[i]:
            tmp += str(j)

for i in range(len(regist)):
    if arr[-1] == regist[i]:
        tmp2 = pow(10, i)

print(int(tmp) * tmp2)