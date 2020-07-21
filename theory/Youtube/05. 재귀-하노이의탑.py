N = int(input())

from_pos = 1
aux_pos = 2
to_pos = 3

def hanoi(N, from_pos, to_pos, aux_pos):
    if N==20:
        return
    if N==1:
        print("원반 1 을 ",from_pos,"에서 ", to_pos,"로 이동.")
        return
    hanoi(N-1,from_pos,aux_pos,to_pos)
    print("원반",N,"을 ",from_pos,"에서 ", to_pos,"로 이동.")
    hanoi(N-1,aux_pos, to_pos, from_pos)

hanoi(N, from_pos, to_pos, aux_pos)