# 슬라이딩 윈도우
arr = [2, 4, 7, 10, 8, 4]
window_size = 3

window_sum, max_sum, start = 0, 0, 0
for end in range(len(arr)):
    window_sum += arr[end]
    if end >= (window_size - 1):
        max_sum = max(max_sum, window_sum)
        window_sum -= arr[start]
        start += 1
print(max_sum)