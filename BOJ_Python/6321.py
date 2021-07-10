# IBM 빼기1
import sys
input = lambda :sys.stdin.readline().rstrip()

for tc in range(int(input())):
    s = input()
    tmp = ''
    for i in range(len(s)):
        if s[i] == 'Z':
            tmp += 'A'
        else:
            tmp += str(chr(int(ord(s[i])) + 1))
    print("String #", end='')
    print(tc + 1)
    print(tmp)
    print()