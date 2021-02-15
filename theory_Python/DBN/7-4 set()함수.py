n = int(input())
parts = set(map(int, input().split()))
print(parts)
m = int(input())
order = list(map(int, input().split()))

for i in order:
    if i in parts:
        print('yes', end=' ')
    else:
        print('no', end=' ')