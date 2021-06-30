# 외계인의 기타 연주
import sys
input = lambda :sys.stdin.readline().rstrip()

line = [[] for _ in range(7)] # 1~6번줄의 음계를 저장할 스택
n, p = map(int, input().split())
cnt = 0

for _ in range(n):
    string, pret = map(int, input().split())

    if len(line[string]) == 0: # 줄의 음계가 비어있다면
        line[string].append(pret) # 프렛 값을 푸시하고 cnt++
        cnt += 1

    else: # 줄에 음계가 있다면
        if line[string][-1] < pret: #peek값과 프렛을 비교하여 들어갈 프렛 값이 크면
            line[string].append(pret) # 그 값을 push후 cnt++
            cnt += 1
        elif line[string][-1] > pret: #만약 peek값보다 작다면
            while line[string]: #일단 와일로 돌려서 pop을 해줘야한다
                if line[string][-1] < pret or line[string][-1] == pret: break
                #언제까지? 프렛값이 peek보다 클때나 혹은 같을 때까지
                line[string].pop()
                cnt += 1
            if len(line[string]) and line[string][-1] == pret: continue # 만약 값이 같으면 push하지 말고 스킵
            line[string].append(pret) # 프렛값이 peek값보다 크다면 push후 cnt++
            cnt += 1
        elif line[string][-1] == pret: # peek값과 프렛값이 같으면 스킵
            continue

print(cnt) # 답 출력