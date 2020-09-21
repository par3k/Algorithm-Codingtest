# 섬의 갯수
'''
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
'''

while True:
    w, h = map(int, input().split())
    visited = [0] * (w * h)
    if w == 0 and h == 0:
        break


    print(w, h)
    print(visited)