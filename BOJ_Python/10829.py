# 이진수 변환
import sys
n = int(sys.stdin.readline().rstrip())
answer = ''


def recursive(n):
    global answer

    if n == 1:
        answer += str(n)
        print(answer[::-1])
        return
    answer += str(n % 2)
    recursive(n // 2)


recursive(n)