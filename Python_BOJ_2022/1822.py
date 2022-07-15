# 차집합
a, b = map(int, input().split())
list_1 = set(map(int, input().split()))
list_2 = set(map(int, input().split()))
diff = list_1 - list_2

if not len(diff):
    print(0)
else:
    print(len(diff))
    answer = list(diff)
    tmp = list()
    for i in sorted(answer):
        tmp.append(str(i))
    print(' '.join(tmp))