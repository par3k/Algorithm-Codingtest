# 떡볶이 떡 만들기

n, m = map(int, input().split())
ddeok = list(map(int, input().split()))

start = 0
end = max(ddeok)

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in ddeok:
        if x > mid:
            total += x - mid


    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)