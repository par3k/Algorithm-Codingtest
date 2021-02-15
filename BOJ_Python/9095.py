# 1,2,3 더하기


def find(n):
    cnt = [0] * 100
    cnt[1] = 1
    cnt[2] = 2
    cnt[3] = 4

    for i in range(4, n+1):
        cnt[i] = cnt[i-1] + cnt[i-2] + cnt[i-3]
    return cnt[n]


nums = []

for _ in range(int(input())):
    n = int(input())
    nums.append(int(n))

for i in range(0, len(nums)):
    print(find(nums[i]))