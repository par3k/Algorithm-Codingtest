# 나무 재테크
import sys
inpud = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, 1, -1]

n, m, k = map(int, input().split()) # 그래프 크기, 나무 갯수, k년후
arr = [list(map(int, input().split())) for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split()) # x, y, 나무의 나이
    tree[x - 1][y - 1].append(z)

graph = [[5 for _ in range(n)] for _ in range(n)] # 그래프를 초기화 시켜줌

for _ in range(k):
    # 봄
    for i in range(n):
        for j in range(n):
            if len(tree[i][j]) <= 0: continue # 나무가 없는 tree 배열은 스킵
            tree[i][j].sort() # 어린 나무 우선으로 양분을 먹기에 오름차순 정렬해줌

            idx = 0

            while idx < len(tree[i][j]):
                if tree[i][j][idx] <= graph[i][j]: # 토양의 양분을 먹을 수 있다면
                    graph[i][j] -= tree[i][j][idx] # 쪽쪽
                    tree[i][j][idx] += 1 # 나이 1살+
                    idx += 1
                # 여름
                else: # 토양의 양분을 먹을 수 없다면
                    die = tree[i][j][idx:]
                    # 그 나무 뒤에있는 모든 나무들 또한 양분을 못 먹어서 죽으니까
                    for now in die: # 죽어서 양분됨
                        graph[i][j] += (now // 2) # 냠냠
                    tree[i][j] = tree[i][j][:idx] # 양분을 먹을 수 있는 나무만 남음
                    break


    # 가을
    for i in range(n):
        for j in range(n):
            child = 0

            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0: # 나무의 나이가 5의 배수라면
                        child += 1 # 애 하나 증가

            if child > 0: # 애가 하나라도 있다면
                for k in range(8): # 팔방에 씨뿌리기
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n: # 그래프 범위내에서
                        for _ in range(child):
                            tree[nx][ny].append(1) # 씨를 뿌려줍니다

    # 겨울
    for i in range(n):
        for j in range(n):
            graph[i][j] += arr[i][j] # 양분 보충

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j]) # tree 그래프에 있는 나무 갯수 출력

print(ans)