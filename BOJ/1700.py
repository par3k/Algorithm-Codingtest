# 멀티탭 스케줄링
import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
cmd = list(map(int, input().split()))
queue = [[] for _ in range(101)]

for idx, val in enumerate(cmd):
    queue[val].append(idx)

plug = {}
ans = 0

for idx, val in enumerate(cmd):
    if len(plug) < N:
        plug[val] = 1
    elif val in plug:
        pass
    else:
        del_idx = idx
        del_val = 101

        for check in plug:
            for check_idx in queue[check]:
                if check_idx > idx:
                    if del_idx < check_idx:
                        del_idx, del_val = check_idx, check
                    break
            else:
                del_val = check
                break

        del plug[del_val]
        plug[val] = 1
        ans += 1

print(ans)