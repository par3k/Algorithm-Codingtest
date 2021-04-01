# AC
import sys
from collections import deque
input = lambda :sys.stdin.readline()

errFlag = False
for _ in range(int(input())):
    p = input() # 수행할 함수
    n = int(input())    # 배열에 숫자 갯수

    arr = input()[1:-2].split(",")

    if arr[0] != '':
        arr = deque(arr)
    else:
        arr = deque()
    direction_Flag=True

    for i in p:
        if i == "R":
            if direction_Flag==True:
                direction_Flag = False
            elif direction_Flag==False:
                direction_Flag = True
        elif i == "D":
            if len(arr) == 0 :
                print("error")
                errFlag = True
                break

            if direction_Flag == True:
                arr.popleft()
            elif direction_Flag==False:
                arr.pop()

    if p.count('R') % 2 != 0:
        arr.reverse()

    if errFlag==False:
        print("[",end="")
        for i in range(len(arr)):
            print(arr[i],end="")
            if i != len(arr)-1:
                print(",",end="")
        print("]")
    errFlag=False


# 1
# DD
# 2
# [1,2]
# error