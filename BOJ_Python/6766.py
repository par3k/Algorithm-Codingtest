import sys
input = lambda : sys.stdin.readline().rstrip()

k = int(input())
a = input().upper()

for i in range(len(a)):
    idx = ord(a[i])
    code = 3 * (i+1) + k
    gazua = idx - code
    if gazua < 65:
        gazua += 26
    print(chr(gazua), end='')
