# 계단 오르기
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

stairs = [0]
visit = [0]

for i in range(n):
    stairs.append(int(input()))

if n >= 1:
    visit.append(stairs[1])

if n >= 2:
    visit.append(stairs[1] + stairs[2])

if n >= 3:
    visit.append(max(stairs[1]+stairs[3], stairs[2]+stairs[3]))

for i in range(4, n+1):
    visit.append(max(visit[i-3] + stairs[i-1] + stairs[i], visit[i-2] + stairs[i]))

print(visit[-1])
