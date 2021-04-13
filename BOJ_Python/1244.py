# 스위치 켜고 끄기
n = int(input())
arr = list(map(int,input().split()))

def womanDo(num):
    left, right = num - 2, num
    arr[num - 1] ^= 1
    while left >= 0 and right < n:
        if arr[left] == arr[right]:
            arr[left] ^= 1
            arr[right] ^= 1
        else:
            break
        left -= 1
        right += 1


for _ in range(int(input())):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(n):
            if (i+1) % num == 0:
                arr[i] ^= 1
    elif sex == 2:
        womanDo(num)

for i in range(0, n, 20):
    print(*arr[i:i+20])