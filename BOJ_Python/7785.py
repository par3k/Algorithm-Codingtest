# 회사에 있는 사람
arr = dict()
for _ in range(int(input())):
    name, action = input().split()
    if action == 'enter':
        arr[name] = True
    else:
        del arr[name]

print("\n".join(sorted(arr.keys(), reverse=True)))