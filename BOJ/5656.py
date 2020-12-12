# 비교 연산자
i = 1
while True:
    num1, ope, num2 = input().strip().split()

    if ope == 'E':
        break

    if ope == '>':
        print(f'Case {i}: ' + str(int(num1) > int(num2)).lower())

    elif ope == '>=':
        print(f'Case {i}: ' + str(int(num1) >= int(num2)).lower())

    elif ope == '<':
        print(f'Case {i}: ' + str(int(num1) < int(num2)).lower())

    elif ope == '<=':
        print(f'Case {i}: ' + str(int(num1) <= int(num2)).lower())

    elif ope == '==':
        print(f'Case {i}: ' + str(int(num1) == int(num2)).lower())

    elif ope == '!=':
        print(f'Case {i}: ' + str(int(num1) != int(num2)).lower())
    i += 1