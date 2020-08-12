# 회의실배정
import sys

N = int(sys.stdin.readline())
time_table = []

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    time_table.append((start, end))

start_time = 0
cnt = 0

time_table = sorted(time_table, key= lambda time : time[0])
time_table = sorted(time_table, key= lambda time : time[1])


for time in time_table:
    if time[0] >= start_time:
        start_time = time[1]
        cnt += 1

print(cnt)
