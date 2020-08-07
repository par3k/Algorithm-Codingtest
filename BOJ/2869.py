# 달팽이는 올라가고 싶다
'''
IDEA
day 1 2m - 1m : 1m
day 2 (1m+2m) - 1m : 2m
day 3 (2m+2m) - 1m : 3m
day 4 (3m+2m) - 1m : 5m end

Recursive

'''



A, B, V = map(int, input().split())

height = 0

calc = (V-B)/(A-B)

if V == 0:
    print('0')
else:
    if calc == int(calc):
        print(int(calc))
    else:
        print(int(calc)+1)



'''
A, B, V = map(int, input().split())

height = A - B
day = 0

while True:
    height = (height + A) - B
    day += 1
    if V == height:
        break
print(day)

제한시간이 0.15초
와일문, 부등호 비교가 있으면 안됨
입력받은 순간 답이 나와야된다.
'''

