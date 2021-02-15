# 암호
import sys
input = lambda : sys.stdin.readline().rstrip()

s = list(map(str, input()))
key = list(map(str, input())) * 100000
arr = list()

for i in range(len(s)):
    if s[i] == " ": arr.append(" ")
    else: arr.append(ord(s[i]) - ord('a') + 1)

for i in range(len(arr)):
    if arr[i] == " ": continue
    if int(arr[i]) - int(ord(key[i]) - ord('a') + 1) <= 0:
        arr[i] = chr(arr[i] + (26 - (ord(key[i]) - ord('a') + 1)) + 96)
    else:
        arr[i] = chr(arr[i] - (ord(key[i]) - ord('a') + 1) + 96)

print(''.join(arr))
