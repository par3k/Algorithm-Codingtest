# 좋은 단어
import sys
input = lambda :sys.stdin.readline().rstrip()
ans = 0

for _ in range(int(input())):
    arr = []
    s = input()
    for i in range(len(s)):
        if len(arr) == 0:
            arr.append(s[i])
        else:
            if arr[-1] == s[i]:
                arr.pop()
            else:
                arr.append(s[i])

    if len(arr) == 0:
        ans += 1
print(ans)