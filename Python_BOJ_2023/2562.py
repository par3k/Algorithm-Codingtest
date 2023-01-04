# 최댓값

max_val = -1
idx = 0
for i in range(9):
    input_val = int(input())
    if max_val < input_val:
        max_val = max(max_val, input_val)
        idx = i + 1

print(max_val)
print(idx)
