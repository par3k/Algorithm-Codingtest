# 너의 이름은 몇 점이니?
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
name = input()
sum = 0

for i in range(n):
    sum += int(ord(name[i]) - ord('A')) + 1

print(sum)