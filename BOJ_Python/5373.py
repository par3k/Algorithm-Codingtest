# 큐빙
import sys
input = lambda : sys.stdin.readline().rstrip()


def cw(arr):
    new_arr = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_arr[i][j] = arr[2 - j][i]
    return new_arr


def ccw(arr):
    new_arr = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_arr[i][j] = arr[j][2 - i]
    return new_arr


def move(cmd):
    global cube
    if cmd == 'U+':
        cube[4][0], cube[3][0], cube[5][0], cube[2][0] = cube[2][0], cube[4][0], cube[3][0], cube[5][0]
        cube[0] = cw(cube[0])
        return

    elif cmd == 'U-':
        cube[5][0], cube[3][0], cube[4][0], cube[2][0] = cube[2][0], cube[5][0], cube[3][0], cube[4][0]
        cube[0] = ccw(cube[0])
        return

    elif cmd == 'D-':
        cube[4][2], cube[3][2], cube[5][2], cube[2][2] = cube[2][2], cube[4][2], cube[3][2], cube[5][2]
        cube[1] = ccw(cube[1])
        return

    elif cmd == 'D+':
        cube[5][2], cube[3][2], cube[4][2], cube[2][2] = cube[2][2], cube[5][2], cube[3][2], cube[4][2]
        cube[1] = cw(cube[1])
        return

    elif cmd == "F+":
        a, b, c = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[0][2][2], cube[0][2][1], cube[0][2][0]
        cube[0][2][2], cube[0][2][1], cube[0][2][0] = a, b, c
        cube[2] = cw(cube[2])
        return

    elif cmd == "F-":
        a, b, c = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[0][2][2], cube[0][2][1], cube[0][2][0]
        cube[0][2][2], cube[0][2][1], cube[0][2][0] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = a, b, c
        cube[2] = ccw(cube[2])
        return

    elif cmd == "B+":
        a, b, c = cube[4][0][0], cube[4][1][0], cube[4][2][0]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
        cube[0][0][2], cube[0][0][1], cube[0][0][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = a, b, c
        cube[3] = cw(cube[3])
        return

    elif cmd == "B-":
        a, b, c = cube[4][0][0], cube[4][1][0], cube[4][2][0]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = cube[1][2][0], cube[1][2][1], cube[1][2][2]
        cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][2][2], cube[5][1][2], cube[5][0][2] = cube[0][0][2], cube[0][0][1], cube[0][0][0]
        cube[0][0][2], cube[0][0][1], cube[0][0][0] = a, b, c
        cube[3] = ccw(cube[3])
        return

    elif cmd == "L+":
        a, b, c = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
        cube[3][2][2], cube[3][1][2], cube[3][0][2] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = a, b, c
        cube[4] = cw(cube[4])
        return

    elif cmd == "L-":
        a, b, c = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[3][2][2], cube[3][1][2], cube[3][0][2]
        cube[3][2][2], cube[3][1][2], cube[3][0][2] = a, b, c
        cube[4] = ccw(cube[4])
        return

    elif cmd == "R+":
        a, b, c = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = a, b, c
        cube[5] = cw(cube[5])
        return
    else:
        a, b, c = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = a, b, c
        cube[5] = ccw(cube[5])
        return


for _ in range(int(input())):
    n = int(input())
    cmd = list(input().split())
    cube = [[['w','w','w'],['w','w','w'],['w','w','w']],
            [['y','y','y'],['y','y','y'],['y','y','y']],
            [['r','r','r'],['r','r','r'],['r','r','r']],
            [['o','o','o'],['o','o','o'],['o','o','o']],
            [['g','g','g'],['g','g','g'],['g','g','g']],
            [['b','b','b'],['b','b','b'],['b','b','b']]]
    for i in cmd:
        move(i)

    for i in range(3):
        ans = ''.join(cube[0][i])
        print(ans)
