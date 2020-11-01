# 팰린드롬인지 확인하기
s = input()
r = list()

for i in range(len(s)-1, -1, -1):
    r.append(s[i])

if s == ''.join(r):
    print(1)
else:
    print(0)
