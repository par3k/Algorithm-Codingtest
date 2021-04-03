#

def calc(ssum):
    q, d, n, p = 0, 0, 0, 0
    while ssum != 0:
        if ssum >= 25:
            q += ssum // 25
            ssum %= 25

        if 10 <= ssum < 25:
            d += ssum // 10
            ssum %= 10

        if 5 <= ssum < 10:
            n += ssum // 5
            ssum %= 5

        if 1 <= ssum < 5:
            p += ssum // 1
            ssum -= p
    return q, d, n, p


for _ in range(int(input())):
    ssum = int(input())
    q, d, n, p = 0, 0, 0, 0
    while ssum != 0:
        if ssum >= 25:
            q += ssum // 25
            ssum %= 25

        if 10 <= ssum < 25:
            d += ssum // 10
            ssum %= 10

        if 5 <= ssum < 10:
            n += ssum // 5
            ssum %= 5

        if 1 <= ssum < 5:
            p += ssum // 1
            ssum -= p
    print(q, d, n, p)

