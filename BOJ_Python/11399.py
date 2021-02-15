# ATM

N = int(input())
Time = list(map(int, input().split()))
Time.sort()

ans = 0
for i in range(N):
    for j in range(N-i):
        ans += Time[j]

print(ans)

'''
업무를 빠르게 처리하는 순서 : 1 2 3 3 4

0 1 2 3 4
ans = 1
ans = 1 + 2
ans = 1 + 2 + 3
ans = 1 + 2 + 3 + 3
ans = 1 + 2 + 3 + 3 + 4 = 13

0 1 2 3
ans = 13 + 1
ans = 13 + 1 + 2
ans = 13 + 1 + 2 + 3
ans = 13 + 1 + 2 + 3 + 3 = 22

0 1 2
ans = 22 + 1
ans = 22 + 1 + 2
ans = 22 + 1 + 2 + 3 = 28

0 1
ans = 28 + 1
ans = 28 + 1 + 2 = 31

0
ans = 31 + 1 = 32

'''