# 6174
import sys
input = lambda : sys.stdin.readline()

for _ in range(int(input())):
    arr = int(input())
    cnt = 0

    if arr == 6174:
        print(0)
    else:
        tmp = sorted(list(str(arr)))
        while True:
            max_tmp = int(''.join(tmp[::-1]))
            min_tmp = int(''.join(tmp[::]))
            ans = max_tmp - min_tmp

            if ans == 6174:
                cnt += 1
                break
            else:
                tmp = sorted(list(str(ans)))
                if len(tmp) < 4:
                    k = len(tmp)
                    tmp += ['0'] * (4 - k)
                tmp.sort()
            cnt += 1
        print(cnt)

