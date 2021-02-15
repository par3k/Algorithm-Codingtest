# 문서검색
import sys
input = lambda :sys.stdin.readline().rstrip()

string = list(input())
i = list(input())

cnt = 0
current_idx = 0

while current_idx < len(string):
    for idx in range(len(i)):
        if current_idx + idx >= len(string):
            current_idx += 1
            break

        if i[idx] != string[current_idx + idx]:
            current_idx += 1
            break

    else:
        cnt += 1
        current_idx += len(i)

print(cnt)