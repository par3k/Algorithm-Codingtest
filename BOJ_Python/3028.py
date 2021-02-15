# 창영마을
import sys
arr = [0] * 3
arr[0] = 1


def shuffle_a(arr):
    arr[0], arr[1] = arr[1], arr[0]
    return arr


def shuffle_b(arr):
    arr[1], arr[2] = arr[2], arr[1]
    return arr


def shuffle_c(arr):
    arr[0], arr[2] = arr[2], arr[0]
    return arr


s = sys.stdin.readline().rstrip()
for i in range(len(s)):
    if s[i] == 'A': shuffle_a(arr)
    elif s[i] == 'B': shuffle_b(arr)
    else: shuffle_c(arr)

for i in range(len(arr)):
    if arr[i] == 1:
        print(i + 1)