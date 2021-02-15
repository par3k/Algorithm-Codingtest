# 로마 숫자
import sys
input = lambda : sys.stdin.readline().rstrip()

num = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
extra = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}

num1, num2 = input(), input()


def toNum(r):
    res = 0
    n = len(r)
    idx = 0

    while idx < n:
        if idx == n - 1:
            res += num[r[idx]]
            break

        flag = True
        if r[idx] == 'I':
            if r[idx + 1] == 'V' or r[idx + 1] == 'X':
                res += extra[r[idx : idx + 2]]
                flag = False
        elif r[idx] == 'X':
            if r[idx + 1] == 'L' or r[idx + 1] == 'C':
                res += extra[r[idx : idx + 2]]
                flag = False

        elif r[idx] == 'C':
            if r[idx + 1] == 'D' or r[idx + 1] == 'M':
                res += extra[r[idx : idx + 2]]
                flag = False

        if not flag:
            idx += 2
        else:
            res += num[r[idx]]
            idx += 1

    return res


a, b = toNum(num1), toNum(num2)
total = a + b
print(total)

ans = ""
total = str(total)
t = len(total)
n = len(total)

while n:
    nums = int(total[t - n])
    if n == 4:
        ans += 'M' * nums
    elif n == 3:
        if nums == 9:
            ans += 'CM'
        elif nums == 4:
            ans += 'CD'
        else:
            if nums >= 5:
                ans += 'D'
            ans += 'C' * (nums % 5)

    elif n == 2:
        if nums == 9:
            ans += 'XC'
        elif nums == 4:
            ans += 'XL'
        else:
            if nums >= 5:
                ans += 'L'
            ans += 'X' * (nums % 5)

    elif n == 1:
        if nums == 9:
            ans += 'IX'
        elif nums == 4:
            ans += 'IV'
        else:
            if nums >= 5:
                ans += 'V'
            ans += 'I' * (nums % 5)
    n -= 1

print(ans)