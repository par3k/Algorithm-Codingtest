# Dates
import sys
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    s = input()
    f = s.find('/') > 0
    a = [ *map(int, s.replace('.', '/').split('/'))]
    print('%02d.%02d.%04d %02d/%02d/%04d' %(a[f], a[1-f], a[2], a[1-f], a[f], a[2]))