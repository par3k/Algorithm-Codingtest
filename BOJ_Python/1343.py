# 폴리오미노
import sys
input = lambda : sys.stdin.readline().rstrip()

data = input().upper()
i = 0

while True:
    if i >= len(data):
        break

    if data[i:i+4] == 'XXXX':
        i += 4
        data = data.replace('X', 'A', 4)
    elif data[i:i+2] == 'XX':
        i += 2
        data = data.replace('X', 'B', 2)
    elif data[i] == '.':
        i += 1
    else:
        data = -1
        break

print(data)