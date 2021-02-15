# 하노이 탑 이동 순서

N = int(input())

from_pos = 1
aux_pos = 2
to_pos = 3


def hanoi(N, from_pos, to_pos, aux_pos):
    if N == 1:
        print(from_pos, to_pos)
        return
    hanoi(N-1,from_pos,aux_pos,to_pos)
    print(from_pos, to_pos)
    hanoi(N-1,aux_pos, to_pos, from_pos)


print(pow(2, N)-1)
hanoi(N, from_pos, to_pos, aux_pos)