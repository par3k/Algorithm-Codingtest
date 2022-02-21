# N과 M(9)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

chk = [False] * (n + 1)
ans = [0] * m

def recursive(depth):
    if depth == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
        
    tmp_num = 0
    for i in range(n):
        if chk[i]:
            continue
        elif tmp_num != nums[i]:
            chk[i] = True
            ans[depth] = nums[i]
            tmp_num = nums[i]
            recursive(depth + 1)
            chk[i] = False

recursive(0)