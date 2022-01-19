# 동전0
n, k = map(int, input().split())
pouch = list()

for _ in range(n):
    pouch.append(int(input()))


def solution(input_val):
    global pouch
    new_pouch = pouch[::-1]
    ans = 0
    for i in range(len(new_pouch)):
        if new_pouch[i] > input_val:
            continue
        else:
            cnt = input_val // new_pouch[i]
            input_val -= new_pouch[i] * cnt
        ans += cnt
    print(ans)


solution(k)