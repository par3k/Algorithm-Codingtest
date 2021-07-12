# 팬그램
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '*': break

    alphabet = [0] * 26

    for i in s:
        if i == ' ': continue

        if alphabet[ord(i) - ord('a')] == 1: continue
        else: alphabet[ord(i) - ord('a')] += 1

    if sum(alphabet) == 26:
        print("Y")
    else:
        print("N")