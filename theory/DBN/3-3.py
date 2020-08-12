N, M = map(int, input().split())
a = []

for i in range(N):
    data = list(map(int, input().split()))
    a.append(min(data))
print(max(a))