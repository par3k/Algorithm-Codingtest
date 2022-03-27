# 카드
import sys
input = lambda:sys.stdin.readline().rstrip()
dic = dict()

for _ in range(int(input())):
    n = int(input())
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

result = sorted(dic.items(), key= lambda item: (-item[1], item[0]))
print(result[0][0])