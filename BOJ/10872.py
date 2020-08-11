#팩토리얼

def pactorial(n):
    if n <= 1:
        return 1
    else:
        return n * pactorial(n-1)

n = int(input())
print(pactorial(n))