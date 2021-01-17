# The Seven Percent Solution
import sys

while True:
    a = list(map(str, sys.stdin.readline().rstrip()))

    if a[0] == "#":
        break

    for i in range(len(a)):
        if a[i] == " ":
            a[i] = "%20"
        elif a[i] == "!":
            a[i] = "%21"
        elif a[i] == "$":
            a[i] = "%24"
        elif a[i] == "%":
            a[i] = "%25"
        elif a[i] == "(":
            a[i] = "%28"
        elif a[i] == ")":
            a[i] = "%29"
        elif a[i] == "*":
            a[i] = "%2a"
        else:
            continue

    print(''.join(a))