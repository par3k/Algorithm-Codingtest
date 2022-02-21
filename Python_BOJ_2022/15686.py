# 치킨배달
import sys
sys.setrecursionlimit(10000001)
# (r1, c1) (r2, c2) >> |r1 - r2| + |c1 - c2|

n, m = map(int, input().split()) # 마을 크기 n x n / 치킨집 갯수
graph = [list(map(int, input().split())) for _ in range(n)]

home, kfc = [], [] # 집과 kfc 좌표 저장할 리스트
ans = 123456789
kfc_nums = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i + 1, j + 1))
        elif graph[i][j] == 2:
            kfc.append((i + 1, j + 1))


def solve(kfc_num, kfc_cnt): # kfc 몇 호점인지 나타내는 숫자, kfc갯수
    global ans
    # 기저조건
    if kfc_num > len(kfc):
        return
    if kfc_cnt == m:
        tmp = 0
        for x, y in home:
            min_distance = 123456789
            for i in kfc_nums: # 선택된 치킨집들
                kfc_x, kfc_y = kfc[i]
                min_distance = min(min_distance, abs(x - kfc_x) + abs(y - kfc_y))
            tmp += min_distance
        ans = min(ans, tmp)
        return

    kfc_nums.append(kfc_num)
    solve(kfc_num + 1, kfc_cnt + 1)
    kfc_nums.pop()
    solve(kfc_num + 1, kfc_cnt)

solve(0, 0)
print(ans)