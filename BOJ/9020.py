# 골드바흐의 추측
import sys
input = lambda : sys.stdin.readline().rstrip()


def prime_list(n):
    data = [True] * n
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if data[i]:
            for j in range(i + i, n, i):
                data[j] = False
    return data


def gold(primes, n):
    i = 0
    while True:
        if primes[n // 2 - i] and primes[n // 2 + i]:
            return (n // 2 - i, n // 2 + i)
        i += 1


a_list = prime_list(10001)
for _ in range(int(input())):
    n = int(input())
    answer = gold(a_list, n)
    print(answer[0], answer[1])