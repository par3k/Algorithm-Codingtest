# 막대기
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

kijoon = stack.pop()
max_height = kijoon # 기둥보다 큰 기둥이 나타날 때 카운트 하기위한 기준
ans = 1

while stack:
    if kijoon < stack[-1] and max_height < stack[-1]:
        max_height = stack[-1]
        ans += 1
        stack.pop()
    else:
        stack.pop()
print(ans)