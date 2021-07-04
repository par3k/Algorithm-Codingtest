# 옥상 정원 꾸미기
import sys
input = lambda :sys.stdin.readline().rstrip()

bdg = list()
for _ in range(int(input())):
    bdg.append(int(input()))

stack = list()
ans = 0

for i in bdg:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    ans += len(stack) - 1

print(ans)