# 이차원 배열과 연산  나중에 다시 풀어본다..
from collections import Counter
r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

r -= 1
c -= 1
time = 0

while time <= 100:
    if r < len(arr) and c < len(arr[0]) and arr[r][c] == k:
        print(time)
        break

    flag = False
    if len(arr) < len(arr[0]):
        flag = True
        arr = list(zip(*arr))

    max_rowlen = 0
    tmp_arr = list()

    for now_row in arr:
        cnt = Counter(now_row)
        if cnt.get(0):
            del cnt[0]
        num_cnt = list(map(list, cnt.items()))
        num_cnt.sort(key = lambda x:(x[1], x[0]))
        tmp_arr.append(list(sum(num_cnt, []))[:100])
        max_rowlen = max(max_rowlen, len(tmp_arr[-1]))

    for i in range(len(tmp_arr)):
        if (len(tmp_arr)) < max_rowlen:
            tmp_arr[i] += [0] * (max_rowlen - len(tmp_arr[i]))

    arr = tmp_arr

    if flag:
        arr = list(zip(*arr))
    time += 1

if time > 100:
    print(-1)