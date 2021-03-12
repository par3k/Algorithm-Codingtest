program = "line"
flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
commands = ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]

# program = "trip"
# flag_rules = ["-days NUMBERS", "-dest STRING"]
# commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]

def solution(program, flag_rules, commands):
    tmp = list()
    for i in range(len(commands)):
        tmp.append(commands[i].split(","))

    cmd = list()
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            cmd.append(tmp[i][j].split(" "))
    print(cmd)

    tmp2 = list()
    for i in range(len(flag_rules)):
        tmp2.append(flag_rules[i].split(","))

    flagR = list()
    for i in range(len(tmp2)):
        for j in range(len(tmp2[i])):
            flagR.append(tmp2[i][j].split(" "))

    print(flagR)
    ans = [False] * len(cmd)
    # 프로그램 이름 체크
    for i in range(len(cmd)):
        if cmd[i][0] == program:
            ans[i] = True

    for i in range(len(cmd)):
        for j in range(1, len(cmd[i])):
            for a in range(len(flagR)):

                if flagR[a][1] == "STRINGS":
                    if cmd[i][j] == flagR[a][0]: # String 커맨드가 있다면
                        if not cmd[i][j+1].isalnum():
                            ans[i] = False
                        elif cmd[i][j + 2] != flagR[a][0]:
                            ans[i] = False

                elif flagR[a][1] == "NUMBERS":
                    if cmd[i][j] == flagR[a][0]:
                        if not cmd[i][j + 1].isalnum():
                            ans[i] = False

                elif flagR[a][1] == "NULL":
                    if cmd[i][j] == flagR[a][0]:
                        if cmd[i][-1] != '-e':
                            ans[i] = False

                elif len(cmd[i]) == 2:
                    ans[i] = False
    print(ans)



solution(program, flag_rules, commands)