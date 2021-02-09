# 잠수함식별
import re, sys

p = re.compile("(100+1+|01)+")
s = sys.stdin.readline().rstrip()

m = p.fullmatch(s)
if (m == None):
    print('NOISE')
else:
    if(m.end() ==len(s)):
        print('SUBMARINE')
    else:
        print('NOISE')

