# 가르침 - 못 풀겠다 시간초과 ㅡ,.ㅡ 자바로 풀었음
import sys
sys.setrecursionlimit(100001)
input = lambda : sys.stdin.readline().rstrip()


def dfs(idx, cnt):
    global max_v, global_flag

    if max_v == n:
        return

    if cnt == k-5:
        global_flag, ans = 1, 0
        for i in range(n):
            flag = 0
            for j in range(len(texts[i])):
                if D[ord(texts[i][j]) - 97]:
                    pass
                else:
                    flag = 1
                    break
            if flag == 0:
                ans += 1
        if ans > max_v:
            max_v = ans
        return

    for i in range(idx, len(l)):
        if not D[ord(l[i]) - 97]:
            cnt += 1
            D[ord(l[i]) - 97] = True
            dfs(i, cnt)
            cnt -= 1
            D[ord(l[i]) - 97] = False
    if global_flag == 0:
        max_v = n


n, k = map(int, input().split())

if k < 5:
    print(0)
else:
    global_flag = 0
    D = [False] * 26
    D[ord('a') - 97], D[ord('c') - 97], D[ord('t') - 97], D[ord('i') - 97], D[ord('n') - 97] = True, True, True, True, True
    l, texts = list(), list()
    max_v = 0

    for _ in range(n):
        text = input()
        text = text[4:len(text) - 4]
        for i in range(len(text)):
            if not D[ord(text[i]) - 97] and text[i] not in l:
                l.append(text[i])
        texts.append(text)

    dfs(0, 0)
    print(max_v)