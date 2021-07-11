# 좀비 떼가 기관총 진지에도 오다니 안풀려
import sys
input = lambda :sys.stdin.readline().rstrip()

l = int(input())
ml, mk = map(int, input().split())
c = int(input())

arr = [0] * l
for i in range(l):
    arr[i] = int(input())

while arr:
    if arr[0] > mk: # 맨 앞에 좀비의 피가 총알 뎀지보다 크면 바로 지뢰를 쓸 수 있는지 봐야함
        if c >= 1: # 지뢰 갯수가 있다면 사용
            arr[0] = 0
            c -= 1
            arr.pop(0)
        else: # 지뢰 없으면 바로 게임 종료
            print("NO")
            exit(0)
    else: # 그 외의 경우는 사격 개시
        if len(arr) >= ml:
            for i in range(ml):
                arr[i] -= mk
        else:
            for i in range(len(arr)):
                arr[i] -= mk

        if arr[0] <= 0: # 사격후 좀비의 피가 0이거나 0보다 작으면
            zombie = arr.pop(0) # popleft

print("YES")