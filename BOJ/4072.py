# Words
import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    a = list(map(str, input().split()))
    if a[0] == '#': break
    ans = list()

    for i in range(len(a)):
        ans.append(a[i][::-1])
    print(' '.join(ans))

