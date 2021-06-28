# 유학 금지

pw = "CAMBRIDGE"
s = input()
ans = ''
for i in range(len(s)):
    if s[i] in pw:
        continue
    else:
        ans += s[i]
print(ans)