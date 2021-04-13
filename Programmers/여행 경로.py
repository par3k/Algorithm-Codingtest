# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]


def solution(tickets):
    routes = dict()
    for from_, to_ in tickets:
        if from_ in routes:
            routes[from_].append(to_)
        else:
            routes[from_] = [to_]

    for key in routes.keys():
        print(key)
        routes[key].sort(reverse=True)

    start = ['ICN']
    answer = list()
    while start:
        now = start[-1]
        if now not in routes or len(routes[now]) == 0: # 다 차면 데이터를 빼서 ans에 넣음
            answer.append(start.pop())
        else:
            start.append(routes[now].pop())

    return answer[::-1]


print(solution(tickets))



# {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']} 입력
# {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']} key순 정렬
# ['SFO', 'ATL', 'SFO', 'ICN', 'ATL', 'ICN']
