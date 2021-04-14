# 퇴장하는 순서
import sys
input = lambda :sys.stdin.readline().rstrip()

INF = int(1e9)
n, k = map(int, input().split())
path = [[INF] * (n) for _ in range(n)]

for i in range(k):
    from_, to_ = map(int, input().split())
    path[from_ - 1][to_ - 1] = 1

for k in range(n): # 플로이드 와샬을 통해서 그래프간 연결을 확인 할 수 있으면 거리를 1로 바꿔줌
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if path[i][k] == 1 and path[k][j] == 1:
                path[i][j] = 1

# print(path)
cnt = [0] * n
for i in range(n):
    for j in range(n): # 거쳐가는 노드들을 전부 카운트 해보는중
        if path[i][j] == 1:  # i에서 j로 이동할 수 있으면 cnt에 i번째와 j번째 column 증가
            cnt[i] += 1
            cnt[j] += 1

# print(answer)
print(cnt.count(n - 1))