# 괄호
def solution(data):
    tmp = []
    for i in range(len(data)):
        if data[i] == '(':
            tmp.append(data[i])
        elif data[i] == ')':
            if len(tmp):
                tmp.pop()
            else:
                print("NO")
                return
    if len(tmp):
        print("NO")
        return
    else:
        print("YES")
        return
            
for _ in range(int(input())):
    solution(list(input()))