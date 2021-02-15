# 복호화

for _ in range(int(input())):
    s = list(map(str, input()))
    arr = [0 for _ in range(26)]

    for i in range(len(s)):
        if s[i] == " ": continue
        arr[ord(s[i]) - 97] += 1
    cnt = 0
    for i in range(26):
        if max(arr) == arr[i]:
            cnt += 1
            tmp = i

    if cnt == 1:
        print(chr(tmp + 97))
    else:
        print('?')
