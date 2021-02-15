# 수리공 항승
import sys
input = lambda : sys.stdin.readline().rstrip()

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

tape = 1
tape_length = arr[0] - 0.5 + L

for i in range(1, N):
    if tape_length < arr[i] + 0.5:
        tape_length = arr[i] - 0.5 + L
        tape += 1

print(tape)