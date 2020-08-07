# ACM 호텔

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    count = 0

    for j in range(1, W+1):
        for i in range(1, H+1):
            count += 1

            if N == count:
                if j < 10:
                    print(f'{i}0{j}')
                else:
                    print(f'{i}{j}')





