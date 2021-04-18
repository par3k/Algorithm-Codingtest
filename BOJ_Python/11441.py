# 누적합
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
numbers = list(map(int, input().split()))


def sum(x, y):
    answer = 0
    for i in range(x - 1, y):
        answer += numbers[i]
    return answer


m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(sum(a, b))