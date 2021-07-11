# 찍기
import sys
input = lambda :sys.stdin.readline().rstrip()

n = int(input())
ans = input()

sang_keun = ['A', 'B', 'C']
chang_young = ['B', 'A', 'B', 'C']
hyun_jin = ['C', 'C', 'A', 'A', 'B', 'B']

nick_name = ['Adrian', 'Bruno', 'Goran']
answer_cnt = [0] * 3

for i in range(len(ans)):
    if i >= len(sang_keun):
        if sang_keun[i % len(sang_keun)] == ans[i]:
            answer_cnt[0] += 1
    else:
        if sang_keun[i] == ans[i]:
            answer_cnt[0] += 1

for i in range(len(ans)):
    if i >= len(chang_young):
        if chang_young[i % len(chang_young)] == ans[i]:
            answer_cnt[1] += 1
    else:
        if chang_young[i] == ans[i]:
            answer_cnt[1] += 1

for i in range(len(ans)):
    if i >= len(hyun_jin):
        if hyun_jin[i % len(hyun_jin)] == ans[i]:
            answer_cnt[2] += 1
    else:
        if hyun_jin[i] == ans[i]:
            answer_cnt[2] += 1


max_val = max(answer_cnt)
print(max_val)

for i in range(3):
    if max_val == answer_cnt[i]:
        print(nick_name[i])
