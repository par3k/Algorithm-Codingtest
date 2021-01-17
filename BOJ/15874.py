# Caesar Cipher

k, l = map(int, input().split())
k %= 26
s = input()

if k == 0: print(s)
else:
    result = ""
    for i in range(l):
        if s[i].isalpha():
            if s[i].isupper():
                a = ord(s[i]) - ord('A')
                a += k
                a %= 26
                result += chr(a + ord('A'))
            else:
                a = ord(s[i]) - ord('a')
                a += k
                a %= 26
                result += chr(a + ord('a'))
        else:
            result += s[i]

    print(result)