# 후위 표기식2
n = int(input())
s = list(map(str, input()))
arr = []
for _ in range(n):
    arr.append(int(input()))

op = "+-*/"
ans = []

for i in s:
    if i in op:
        tmp1 = ans.pop()
        tmp2 = ans.pop()

        if i == '+':
            res = tmp1 + tmp2
        elif i == '-':
            res = tmp2 - tmp1
        elif i == '*':
            res = tmp1 * tmp2
        else:
            res = tmp2 / tmp1
        ans.append(res)

    else:
        ans.append(arr[ord(i) - ord('A')])
print("%.2f" %ans[0])