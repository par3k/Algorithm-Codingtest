N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[N-1]
second = data[N-2]
# ans = 0 # 1안

# while True:
#     for i in range(K):
#         if M == 0:
#             break
#         ans += first
#         M -= 1
#     if M == 0:
#         break
#     ans += second
#     M -= 1
#
# print(ans)

cnt = int(M/(K+1)) * K # 2안
cnt += M % (K+1)

ans = 0
ans += cnt * first
ans += (M-cnt) * second
print(ans)