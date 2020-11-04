s=" try hello world "

def solution(s):
    s=s.split(' ')
    print(s)
    a=[]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if i%2 == 0:
                a.append(s[j][i].upper())
            else:
                a.append(s[j][i].lower())
        a.append(" ")
    a="".join(a)
    return a
print(solution(s))
