# 알파벳 거리
import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    tmp = list()
    s = list(map(str, input().split()))

    for i in range(len(s[0])):
        a = ord(s[1][i]) - ord(s[0][i])
        if a < 0: a += 26
        tmp.append(a)
        
    print('Distances:', end=' ')
    for i in tmp: print(i, end=' ')
    print()