# 나는 친구가 적다 (Small)

s = input()
k = input()

ss = ''
for i in range(len(s)):
    if s[i].isdigit():
        continue
    else:
        ss += s[i]

if k in ss:
    print(1)
else:
    print(0)