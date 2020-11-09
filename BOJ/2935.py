# 소음
import sys
input = lambda : sys.stdin.readline().rstrip()

arr = list()
for i in range(3):
    arr.append(input())

if arr[1] == '*':
    print(int(arr[0]) * int(arr[2]))
elif arr[1] == '+':
    print(int(arr[0]) + int(arr[2]))
