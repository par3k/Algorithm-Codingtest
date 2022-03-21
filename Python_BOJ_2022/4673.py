# 셀프 넘버
def solution(n):
    answer = n
    for i in range(0, len(str(n))):
        answer += int(n/10 ** i) % 10
    return answer

lis = []
for i in range(1, 10001):
    lis.append(solution(i))

for i in range(1, 10001):
    if i not in lis:
        print(i)