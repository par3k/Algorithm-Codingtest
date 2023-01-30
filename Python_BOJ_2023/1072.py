# 게임
x, y = map(int, input().split())

def get_percentage(n1, n2):
    return int((n1 * 100) // n2)

z = get_percentage(y, x)

if z >= 99:
    print(-1)
else:
    ans = 0
    start = 1
    end = 10 ** 9
    while start <= end:
        mid = (start + end) // 2
        if get_percentage((y + mid), (x + mid)) > z:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    print(ans)