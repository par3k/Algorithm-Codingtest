program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -n 100 -s hi -e", "lien -s Bye"]
# commands = ["line -s 123 -n HI", "line fun"]

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

    flagRule = list()
    for i in range(len(tmp2)):
        for j in range(len(tmp2[i])):
            flagRule.append(tmp2[i][j].split(" "))
    print(flagRule)

    ans = [False] * len(cmd)
    # 프로그램 이름 체크
    for i in range(len(cmd)):
        if cmd[i][0] == program:
            ans[i] = True

    for i in range(len(cmd)):
        for j in range(1, len(cmd[i])):

            if cmd[i][j] == '-s': # -s 커맨드가 있다면
                if not cmd[i][j + 1].isalnum(): # 숫자, 알파벳으로 이루어진 문자열인지 확인
                    ans[i] = False
            elif cmd[i][j] == '-n': # -n 커맨드가 있다면
                if not cmd[i][j + 1].isdigit(): # 숫자로 이루어졌는지 확인
                    ans[i] = False
            elif cmd[i][j] == '-e':
                if cmd[i][-1] != '-e':
                    ans[i] = False

            elif len(cmd[i]) == 2:
                ans[i] = False
    print(ans)



solution(program, flag_rules, commands)