# 자바 vs 씨쁠쁠
import sys
s = sys.stdin.readline().rstrip()
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def tojava(text):
    if text[0] == "_" or text[-1] == "_" or "__" in text:
        return "Error!"

    ans = ""
    flag = False

    for i in text:
        if i in upper:
            return "Error!"

        if i == "_":
            flag = True
            continue

        if flag == True:
            ans += i.upper()
            flag = False
            continue

        ans += i
    return ans


def tocpp(text):
    if text[0] in upper:
        return "Error!"

    ans = ""
    for i in text:
        if i in upper:
            ans += "_" + i.lower()
        else:
            ans += i
    return ans


if "_" in s:
    print(tojava(s))
else:
    print(tocpp(s))