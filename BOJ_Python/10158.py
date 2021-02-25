# 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t) // w
b = (q + t) // h

if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)


# w, h = map(int, input().split())
# p, q = map(int, input().split())
# t = int(input())
#
# dx, dy = [1, -1, -1, 1], [1, 1, -1, -1]
# cnt = 0
# dir = 0
#
# while True:
#     if t == cnt: break;
#     cnt += 1
#     new_p, new_q = p + dx[dir], q + dy[dir]
#
#     if 0 >= new_p or new_p >= w: # 왼쪽 오른쪽 벽에 부딫힐때
#         if dir == 0: dir = 1
#         elif dir == 1: dir = 0
#         elif dir == 2: dir = 3
#         elif dir == 3: dir = 2
#
#     if 0 >= new_q or new_q >= h: # 아래 위 벽에 부딫힐때
#         if dir == 0: dir = 3
#         elif dir == 1: dir = 2
#         elif dir == 2: dir = 1
#         elif dir == 3: dir = 0
#
#     p, q = new_p, new_q
#
# print(p, q)


