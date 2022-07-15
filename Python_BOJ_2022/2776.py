# 암기왕
import sys

input = lambda : sys.stdin.readline()

for _ in range(int(input())):
    n = int(input())
    note_1 = set(map(int, input().split()))
    m = int(input())
    tmp = list(map(int, input().split()))

    for i in tmp:
        print(1 if i in note_1 else 0)
