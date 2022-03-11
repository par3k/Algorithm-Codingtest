# 2진수 뒤집기
binary = list(map(str, format(int(input()), 'b')))
ans = int(''.join(binary[::-1]), 2)
print(ans)