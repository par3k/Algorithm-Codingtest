s = list(input())

arr = [0] * 26
for i in range(len(s)):
    arr[ord(s[i]) - ord('A')] += 1

tmp = 0
idx = 0
for i in range(26):
    if arr[i] == 0: continue
    elif arr[i] > tmp:
        tmp = arr[i]
        idx = i

print(tmp, chr(idx + ord('A')))