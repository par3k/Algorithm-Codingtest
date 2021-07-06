# https://programmers.co.kr/learn/courses/30/lessons/12973

s = 'baabaa'
# 답 : 1


def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0: # 값이 없으니 하나는 넣어
            stack.append(s[i])
        else:
            if stack[-1] == s[i]: # 제일 위의 Peek값과 지금 꺼낸 값이 같다면
                stack.pop() # pop
            else:
                stack.append(s[i]) # Peek값과 다르면 push한다

    answer = 0
    if len(stack) == 0: # 스택이 비어있다 == 모든 문자열이 쌍을 이루고 pop되서 사라졌다
        answer = 1
    return answer


print(solution(s))