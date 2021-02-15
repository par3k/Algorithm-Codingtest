# 여행 가자
import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(100001)

n = int(input()) # 도시의 수
m = int(input()) # 여행 계획에 속한 도시들의 수

visited = [0 for _ in range(n)]

network = list()
for _ in range(n):
    network.append(list(map(int, input().split())))

travel_city = list(map(int, input().split()))


def dfs(start):
    visited[start] = 1
    for idx, j in enumerate(network[start]):
        if j == 1 and visited[idx] == 0:
            visited[idx] = 1
            dfs(idx)


dfs(travel_city[0] - 1)

if 0 not in visited:
    print('YES')
    exit()

for i in travel_city:
    if visited[i-1] == 0:
        print('NO')
        exit()
print('YES')