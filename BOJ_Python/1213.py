# 팰린드롬 만들기
import sys
names = sys.stdin.readline().rstrip()
alpha_cnt = [0 for _ in range(26)]

for i in names:
    alpha_cnt[ord(i) - 65] += 1

odd = 0
odd_alpha = ''
alpha = ''

for i in range(26):
    if alpha_cnt[i] % 2 == 1:
        odd += 1
        odd_alpha += chr(i + 65)

    alpha += chr(i + 65) * (alpha_cnt[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha + odd_alpha + alpha[::-1])