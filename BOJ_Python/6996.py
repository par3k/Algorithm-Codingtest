# 애너그램
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    a, b = map(str, input().split())
    a_alphabet, b_alphabet = [0] * 26, [0] * 26

    for i in range(len(a)):
        a_alphabet[ord(a[i]) - 97] += 1

    for i in range(len(b)):
        b_alphabet[ord(b[i]) - 97] += 1

    if a_alphabet == b_alphabet:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')