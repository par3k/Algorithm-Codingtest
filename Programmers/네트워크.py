import sys
sys.setrecursionlimit(10001)

n = 4
computers = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]


def find(arr, x):
    if arr[x] == x:
        return x
    else:
        arr[x] = find(arr, arr[x])
    return arr[x]


def union(arr, x, y):
    x = find(arr, x)
    y = find(arr, y)
    if x < y:
        arr[y] = x
    else:
        arr[x] = y


def solution(n, computers):
    parent = [i for i in range(n + 1)]

    tmp = []
    for i in range(n):
        for j in range(n):
            if i == j: continue # 자기 자신은 skip
            if computers[i][j] == 1: # 연결된 노드 번호를 찾아서
                tmp.append([i + 1, j + 1]) # 양방향이므로 저장
                tmp.append([j + 1, i + 1])
    tmp.sort(key = lambda x : x[0]) # 중복을 제거하기 위해 사전 준비 (x, y)에서 x기준 정렬

    tmp2 = []
    for i in tmp:
        if len(tmp2) == 0: # tmp2가 비어있으면 push
            tmp2.append(i)
        if tmp2[-1] == i: # tmp2의 Peek와 값이 같으면 넣지 않음
            continue
        else: # 다르다면 push
            tmp2.append(i)

    for i in tmp2: # 중복 처리된 값을 갖고 유니온-파인드
        a, b = i
        union(parent, a, b)

    answer = set() # 리스트를 set해주면 중복된 부모 값이 사라지므로 노드끼리 연결된 덩어리 수가 도출된다.
    for i in range(1, len(parent)):
        answer.add(find(parent, parent[i])) # parent의 부모 노드를 set에 add
    return len(answer)


print(solution(n, computers))