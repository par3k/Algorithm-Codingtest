import sys
input = lambda :sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = list(map(str, input()))
    ans = 0
    cnt = 1
    for i in s:
        if i == 'O':
            ans += cnt
            cnt += 1
        elif i == 'X':
            cnt = 1
    print(ans)