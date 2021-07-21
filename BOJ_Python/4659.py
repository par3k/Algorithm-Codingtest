# 비밀번호 발음하기

moeun = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    flag = True

    if s == 'end': break

    tmp = ''
    cnt, cons_repeat = 0, 0
    repeat = 0
    for i in s:
        if i in moeun:
            repeat = 0
            cnt += 1
            cons_repeat += 1
            if cons_repeat >= 3:
                flag = False
            if tmp == i:
                if i == 'e' or i == 'o':
                    continue
                else:
                    flag = False
        else:
            repeat += 1
            cons_repeat = 0
            if repeat >= 3:
                flag = False
            if tmp == i:
                flag = False
        tmp = i
    if cnt < 1:
        flag = False

    if not flag:
        print(f'<' + s + '> is not acceptable.')
    else:
        print(f'<' + s + '> is acceptable.')