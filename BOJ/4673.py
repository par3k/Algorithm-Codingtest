# 셀프 넘버

def d(n):
    ans = n
    for i in range(0, len(str(n))):
        ans += int(n/10 ** i) % 10
    return ans

number = list()

for i in range(1, 10001):
    number.append(d(i))
# print(number)

for i in range(1, 10001):
    if i not in number:
        print(i)