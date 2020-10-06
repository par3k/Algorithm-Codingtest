# 택배
import sys
input = lambda : sys.stdin.readline().rstrip()

n, c = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key=lambda x:x[1])

truck = [0] * (n+1)
ans = 0

for i in range(m):
    get = 0
    from_pack = arr[i][0]
    to_pack = arr[i][1]
    val_pack = arr[i][2]

    for j in range(from_pack, to_pack):
        get = max(get, truck[j])

    get = min(c - get, val_pack)
    ans += get

    for j in range(from_pack, to_pack):
        truck[j] += get

print(ans)