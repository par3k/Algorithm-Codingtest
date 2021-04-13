import heapq, sys
input = lambda :sys.stdin.readline().rstrip()
INF = int(1e9)


def dijkstra(s, limit):
    queue = list()
    distance = [INF] * (n + 1)
    heapq.heappush(queue, (0, s))
    distance[s] = 0

    while queue:
        cost, curr = heapq.heappop(queue)
        if distance[curr] < cost: continue

        for i in graph[curr]:
            if i[0] > limit:
                if cost + 1 < distance[i[1]]:
                    distance[i[1]] = cost + 1
                    heapq.heappush(queue, (cost + 1, i[1]))
                else:
                    if cost < distance[i[1]]:
                        distance[i[1]] = cost
                        heapq.heappush(queue, (cost, i[1]))

    if distance[n] > k:
        return False
    else:
        return True


n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    from_, to_, weight = map(int, input().split())
    graph[from_].append((weight, to_))
    graph[to_].append((weight, from_))

left, right = 0, 1000001
ans = INF

while left <= right:
    mid = (left + right) // 2
    flag = dijkstra(1, mid)
    if flag:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

if ans == INF:
    print(-1)
else:
    print(ans)


# [알고리즘]
#
# 알고리즘 전체 과정을 대략적으로 말씀드리면 이분 탐색을 통해 케이블 기준 가격을 정한 후
# 다익스트라를 수행함으로써 1번과 N번 컴퓨터를 이을 수 있는지 판단합니다.
# 세부적인 과정은 다음과 같습니다.

# 1. 이분 탐색을 수행하기 위해 left, right 값을 0과 1000001로 초기화합니다.
# 2. left와 right를 통해 mid 값을 구한 후 다익스트라를 수행합니다.
# 3. 다익스트라 수행은 기존의 다익스트라와 달리 최소 거리를 구하는 것이 아니라
# 1번과 N번을 연결할 수 있는지 구하는 것이 핵심입니다.
# 따라서 거리 값은 mid 값을 넘긴 케이블의 수입니다.
#
# 4. 위 과정을 left 값이 right 값보다 클 때까지 반복합니다.
# 5. 최종적으로 구한 결과를 출력합니다.