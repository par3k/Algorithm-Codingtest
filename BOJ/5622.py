# 다이얼

n = input().upper()
time = 0

for i in range(len(n)):
    if n[i] == 'A' or n[i] == 'B' or n[i] == 'C':
        time += 3
    elif n[i] == 'D' or n[i] == 'E' or n[i] == 'F':
        time += 4
    elif n[i] == 'G' or n[i] == 'H' or n[i] == 'I':
        time += 5
    elif n[i] == 'J' or n[i] == 'K' or n[i] == 'L':
        time += 6
    elif n[i] == 'M' or n[i] == 'N' or n[i] == 'O':
        time += 7
    elif n[i] == 'P' or n[i] == 'Q' or n[i] == 'R' or n[i] == 'S':
        time += 8
    elif n[i] == 'T' or n[i] == 'U' or n[i] == 'V':
        time += 9
    elif n[i] == 'W' or n[i] == 'X' or n[i] == 'Y' or n[i] == 'Z':
        time += 10
    elif n[i] =='1':
        time += 2
    else:
        time += 11
print(time)