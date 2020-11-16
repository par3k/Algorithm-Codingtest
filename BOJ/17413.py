# 단어 뒤집기2
import sys
input = lambda : sys.stdin.readline().rstrip()

ans = ''
flag = 0
word = ''
for c in input():
    if c == '<':
        flag ^= 1
        ans += word
        word = '<'
    elif c == '>':
        flag ^= 1
        ans += (word + '>')
        word = ''
    elif c == ' ':
        ans += (word + ' ')
        word = ''
    else:
        if flag:
            word += c
        else:
            word = c + word

if word:
    ans += word

print(ans)