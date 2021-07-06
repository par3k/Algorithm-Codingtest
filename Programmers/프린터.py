
priorities = [1, 1, 9, 1, 1, 1]
location = 0
# 답 : 5


def solution(priorities, location):
    a = dict()
    for i in range(len(priorities)):
        a[i] = [priorities[i], False]
    a[location][1] = True # location 값의 False를 True로 바꾼다.
    # 나중에 answer에 출력된 순서대로 저장된 리스트에서 True 값의 idx를 찾아주기 위함

    tmp = []
    for i in range(len(a)):
        tmp.append(a[i])

    answer = []
    while tmp:
        if tmp[0][0] < max(tmp, key = lambda x: x[0])[0]:
            tmp.append(tmp.pop(0)) # 내부에 popleft 값보다 큰값이 있다면 이 값은 맨뒤로 보낸다.
        else:
            answer.append(tmp.pop(0)) # 그 외에는 출력했으니 출력한 순서를 알 수 있게 answer에 저장한다.

    for idx in range(len(answer)):
        if answer[idx][1]: # 출력된 리스트 값중 True인 값을 찾아 idx를 출력한다.
            return idx + 1


print(solution(priorities, location))