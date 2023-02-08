# 한수

# 1은 한수, 123 한수
x = int(input())

def chk(num):
    if num < 10:
        return True
    tmp_arr = list(map(int, str(num)))
    d = tmp_arr[1] - tmp_arr[0] # 공차
    idx = 0

    while True:
        if idx == len(tmp_arr) - 1:
            break
        
        if tmp_arr[idx] + d != tmp_arr[idx + 1]:
            return False
        idx += 1

    return True

answer = list()
for i in range(1, x + 1):
    if chk(i):
        answer.append(i)

print(len(answer))