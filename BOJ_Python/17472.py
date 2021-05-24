# 다리 만들기 2
import sys, math
from collections import deque, defaultdict
input = lambda :sys.stdin.readline().rstrip()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(start, graph, continent_num): # 대륙별로 라벨링하기
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()
        graph[x][y] = continent_num

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = continent_num
                    queue.append([nx, ny])


def get_distance(graph): # 각 섬별로 최소거리를 구해보자
    table = defaultdict(lambda : math.inf) # 최소 거리 저장을 위해 딕셔너리 생성, 기본값은 무한대
    iters = [graph, list(map(list, zip(*graph)))]

    for each_maps in iters:
        for x in range(len(each_maps)):
            continent = None
            checked = set()

            for y in range(1, len(each_maps[0])):
                if each_maps[x][y] == 0 and each_maps[x][y - 1] != 0: # 섬 > 바다로 바뀌는 순간 섬의 마지막 좌표 기억
                    continent = y - 1

                if each_maps[x][y] != 0 and continent is not None: # 바다 > 섬으로 바뀌면서 이전에 통과한 섬이 있다면
                    distance = y - continent - 1 # 이전 섬과 현재 섬 거리 계산

                    if distance >= 2 and each_maps[x][y] not in checked: # 거리가 2이상, 현재 섬이 아직 거리 계산을 안했다면

                        small = min(each_maps[x][continent], each_maps[x][y])
                        large = max(each_maps[x][continent], each_maps[x][y])
                        table[(small, large)] = min(table[(small, large)], distance) # 섬과 섬의 거리를 최솟값으로 업데이트 한다.

                    checked.add(each_maps[x][y]) # 현재 섬의 라벨 저장
    return table


def find(x, parent): # 유니온 파인드
    if x == parent[x]:
        return x
    p = find(parent[x], parent)
    parent[x] = p
    return p


def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    parent[y] = x


def get_min_distance(table, continent):
    table = sorted(list(table.items()), key = lambda x: x[1]) # 거리 짧은 순서대로 정렬
    ans = 0

    parent = {i : i for i in range(2, max(continent) + 1)}

    for (x, y), val in table:
        if find(x, parent) != find(y, parent):
            union(x, y, parent)
            ans += val
        if len(set([find(i, parent) for i in parent])) == 1: # 모든섬이 연결되어 있다면 부모는 1개니까 길이가 1인경우는 모두 연결 되었다는 소리다
            return ans
    return -1


continent_num = 2 # 대륙 라벨링 섬은 1이므로 2부터 라벨링 시작
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            bfs((i, j), graph, continent_num)
            continent_num += 1

print(get_min_distance(get_distance(graph), set(range(2, continent_num))))