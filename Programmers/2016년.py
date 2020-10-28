a, b = map(int, input().split())

day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
month = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]

print(day[(sum(month[:a-1]) + b) % 7])