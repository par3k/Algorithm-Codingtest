# 단어 나누기

s = list(map(str, input()))
arr = list()

for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        tmp = s[:i]
        tmp2 = s[i:j]
        tmp3 = s[j:]
        # 역전
        tmp.reverse()
        tmp2.reverse()
        tmp3.reverse()
        # 합치기
        result = tmp + tmp2 + tmp3
        arr.append(''.join(result))
print(min(arr))