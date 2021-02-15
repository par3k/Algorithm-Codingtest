# 8진수, 10진수, 16진수

s = input()
print(int(s[2:], 16) if s[1]=='x' else int(s[1:], 8) if s[0]=='0' else s)