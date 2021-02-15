# 팰린드롬

for _ in range(int(input())):
    s = list(map(str, input().lower()))
    print('Yes' if s[::] == s[::-1] else 'No')