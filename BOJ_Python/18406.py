# 럭키 스트레이트
import sys
s = list(str(sys.stdin.readline().rstrip()))
left, right = 0, 0

for i in range(int(len(s) // 2)):
    left += int(s[i])

for j in range(int(len(s) // 2), len(s)):
    right += int(s[j])

if left == right:
    print("LUCKY")
else:
    print("READY")