# 듣보잡
n, m = map(int, input().split()) # 듣, 보

never_hear_see = {}
ans = []

for i in range(n + m):
    name = input()
    if name in never_hear_see:
        ans.append(name)
    else:
        never_hear_see[name] = 1
ans.sort()
print(len(ans))
for i in ans:
    print(i)