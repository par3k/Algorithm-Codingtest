won = int(input())
sea = int(input())
sang = int(input())
seung = int(input())
kang = int(input())

if won < 40:
    won = 40
if sea < 40:
    sea = 40
if sang < 40:
    sang = 40
if seung < 40:
    seung = 40
if kang < 40:
    kang = 40

sum = won + sea + sang + seung + kang
avg = sum / 5

print(int(avg))
