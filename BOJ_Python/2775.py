# 부녀회장이 될테야

T = int(input())

for i in range(T):
    a = int(input())
    b = int(input())
    people = [i for i in range(1, b+1)] # 0 floor

    for _ in range(a):
        for room_num in range(1, b):
            people[room_num] += people[room_num - 1]
    print(people[-1])