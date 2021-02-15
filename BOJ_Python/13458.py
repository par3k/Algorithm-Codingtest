# 시험 감독
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

ans = n # 총 감독관 수

for group in a:
    group -= b # 총 감독관이 마킹하는 학생 일단 빼주 시작
    if group > 0:
        if group % c:
            ans += (group // c + 1)
        else:
            ans += (group // c)

print(ans)