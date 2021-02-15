# 뒤집힌 덧셈
import sys
input = lambda : sys.stdin.readline().rstrip()

arr = list(map(str, input().split()))
x, y = arr[0], arr[1]


def Rev(n):
    return str(n[::-1])


a = int(Rev(x))
b = int(Rev(y))

print(int(Rev(str(a + b))))
