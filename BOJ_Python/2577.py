a = int(input())
b = int(input())
c = int(input())

total = str(a * b * c)
total_list = []

for i in range(len(total)):
    total_list.append(total[i])

cnt = 0

while cnt <= 9:
    num = total_list.count(str(cnt))
    cnt += 1
    print(num)