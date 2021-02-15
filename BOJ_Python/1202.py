# 보석 도둑
import sys
from queue import PriorityQueue
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
jew = []
for i in range(n):
    jew.append(list(map(int, input().split())))
bag = []
for i in range(k):
    bag.append(int(input()))
jew.sort(reverse=True, key=lambda x:x[1])
for i in range(n):
    jew[i].insert(0, i)

jew.sort(key=lambda x:x[1])
bag.sort()
q = PriorityQueue()

idx = 0
sum = 0

for i in range(k):
    while idx < n and bag[i] >= jew[idx][1]:
        q.put((jew[idx][0], jew[idx][2]))
        idx += 1
    if not q.empty():
        sum += q.get()[1]

print(sum)