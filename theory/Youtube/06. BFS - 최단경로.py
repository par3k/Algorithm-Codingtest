import queue

adj = { # 입력 그래프
    'a':['b', 'c'],
    'b':['a', 'd', 'e'],
    'c':['a', 'e'],
    'd':['b'],
    'e':['b', 'c', 'f'],
    'f':['e', 'g'],
    'g':['f', 'h'],
    'h':['g']
    }


def bfs(adj, start): # adj 입력 그래프, start 탐색 시작할 노드
    visited = set() # 어떤 정점을 방문했는지 표시하기위해 visited 를 집합으로 표시
    tovisit = queue.Queue() # 방문예정목록을 queue로 관리
    tovisit.put(start) # 시작 정점 start를 tovisit 맨 처음에 넣어줌

    while not tovisit.empty(): # 방문예정목록이 빌때까지 정점 방문을 계속한다
        u = tovisit.get() # 방문예정목록에서 노드를 하나 꺼내 u 에 넣습니다.
        if u in visited: # 정점 u를 이미 방문했다면 무시한다
            continue
        visited.add(u) # 집합 visited에 노드 u를 넣어서 u가 이미 방문한 노드임을 나타낸다
        print("visit : ",u)

        for v in adj[u]: # 노드 u의 이웃 노드중에 아직 방문하지 않은 노드를 방문예정목록에 넣어준다
            if v not in visited:
                tovisit.put(v)


print(bfs(adj, 'a'))