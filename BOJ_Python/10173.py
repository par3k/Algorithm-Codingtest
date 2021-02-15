# 니모를 찾아서
name = [['n', 'N'], ['e', 'E'], ['m', 'M'], ['o', 'O']]

while True:
    s = input()
    if s == 'EOI':
        break
    cnt, j = 0, 0
    while j < len(s):
        if s[j] in name[cnt]:
            cnt += 1
            if cnt == 4:
                print('Found')
                break
        else:
            cnt = 0
        j += 1
    else:
        print('Missing')