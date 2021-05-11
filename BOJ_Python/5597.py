# 과제 안 내신 분..?
import sys
check = [0] * 30

for _ in range(28):
    check[int(sys.stdin.readline().rstrip()) - 1] = 1

for i in range(30):
    if check[i] == 0:
        print(i + 1)
