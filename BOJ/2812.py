# 크게 만들기
import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
input_tmp = list(input())
stack = []
cnt = 0

for i in range(n):
    while stack and cnt < k and stack[-1] < input_tmp[i]:
        stack.pop()
        k -= 1
    stack.append(input_tmp[i])

while cnt < k:
    stack.pop()
    k -= 1

for i in range(len(stack)):
    print(stack[i], end='')


'''
6 2
362514
'''