# 가장 긴 팰린드롬 부분 문자열
import sys
input = lambda : sys.stdin.readline().rstrip()


def longesPalindrome(s):
    t = '#'.join('({})'.format(s))
    n = len(t)
    p = [0] * n
    c = r = 0

    for i in range(1, n- 1):
        p[i] = (r >i) and min(r - i, p[2 * c - i])

        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        if i + p[i] > r:
            c, r = i, i + p[i]

    return max(p)


s = input()

print(longesPalindrome(s))