# 창영이의 일기장
s, p, i = input(), "aeiou", 0
while i < len(s):
    print(s[i], end='')
    if p.find(s[i]) > -1:
        i += 2
    i += 1
