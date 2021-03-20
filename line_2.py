# inp_str = "AaTa+!12-3" # [2]
# inp_str = "aaaaZZZZ)" #[2, 3, 4]
# inp_str = "CaCbCgCdC888834A" #[1, 4, 5]
# inp_str = "UUUUU" #[1, 3, 4, 5]
# inp_str = "ZzZz9Z824" # [0]


def solution(inp_str):
    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nom = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    tuk = "~!@#$%^&*"

    arr = inp_str
    ans = list()

    if 8 > len(arr) or len(arr) > 15:
        ans.append(1)

    tmp = list()
    for i in range(len(arr)):
        if arr[i] in cap: continue
        elif arr[i] in nom: continue
        elif arr[i] in num: continue
        elif arr[i] not in tuk:
            tmp.append(i)

    if len(tmp) != 0:
        ans.append(2)

    tmp = set()

    for i in range(len(arr)):
        tmp.add(arr[i])
    tmp = list(tmp)


    res1, res2, res3, res4 = 0, 0, 0, 0
    for i in range(len(tmp)):
        if tmp[i] in cap:
            if res1 == 1: continue
            res1 += 1
    for i in range(len(tmp)):
        if tmp[i] in nom:
            if res2 == 1: continue
            res2 += 1
    for i in range(len(tmp)):
        if tmp[i] in num:
            if res3 == 1: continue
            res3 += 1
    for i in range(len(tmp)):
        if tmp[i] in tuk:
            if res4 == 1: continue
            res4 += 1

    ans2 = res1 + res2 + res3 + res4
    if ans2 < 3:
        ans.append(3)





    flag = True
    for i in inp_str:
        if flag:
            if arr.count(i) >= 5:
                ans.append(5)
                flag = False

    if len(ans) == 0:
        ans.append(0)
    print(ans)


solution(inp_str)


# 문제 설명
#
# 어떤 메신저 회사에서는 해킹으로부터 고객들을 보호하기 위해, 신규 아이디의 password가 다음 규칙을 만족하도록 강제하고 있습니다.
# 8 ≤ password 길이 ≤ 15
# password는 아래 4 종류의 문자 그룹을 제외한, 다른 어떤 문자도 포함해서는 안됩니다.
# [1] 알파벳 대문자(A~Z)
# [2] 알파벳 소문자(a~z)
# [3] 숫자(0~9)
# [4] 특수문자(~!@#$%^&*)
# password는 (2.)에서 명시된 4 종류의 문자 그룹 중에서 3 종류 이상을 포함해야 합니다.
#     password에 어떤 문자라도 같은 문자가 4개 이상 연속될 수 없습니다.
#     password에 어떤 문자라도 같은 문자가 5개 이상 포함될 수 없습니다.
#     고객들이 password로 사용하기 위해 입력한 문자열 inp_str가 매개변수로 주어집니다. 이때, 위에서 나열한 규칙들 중 위배되는 규칙들의 번호를 배열에 담아 오름차순 정렬하여 return 하도록 solution 함수를 완성해주세요. 만약 위배된 규칙이 하나도 없다면, 0을 담아서 return 합니다.
# 제한사항
# 1 ≤ inp_str의 길이 ≤ 1,000,000
# inp_str는 알파벳 대문자(A~Z), 알파벳 소문자(a~z), 숫자(0~9), 특수문자(~!@#$%^&*()-_=+)의 조합으로 구성되는 문자열입니다.
# password로 허용되지 않는 특수문자(()-_=+)가 inp_str에는 나타날 수 있습니다.
#     입출력 예
# inp_str	result
# "AaTa+!12-3"	[2]
# "aaaaZZZZ)"	[2, 3, 4]
# "CaCbCgCdC888834A"	[1, 4, 5]
# "UUUUU"	[1, 3, 4, 5]
# "ZzZz9Z824"	[0]
# 입출력 예 설명
# 입출력 예 #1
# "AaTa+!12-3"
# 허용되지 않는 특수문자(+, -)가 포함되어 있습니다.
# 2번 규칙에 위배됩니다.
#     입출력 예 #2
# "aaaaZZZZ)"
# 허용되지 않는 특수문자())가 포함되어 있습니다.
# 2번 규칙에 위배됩니다.
# 4 종류의 문자 그룹 중에서 3종류 이상이 포함되어 있지 않습니다.
# 3번 규칙에 위배됩니다.
# 같은 문자가 4개 이상 연속됩니다.(a, Z)
# 4번 규칙에 위배됩니다.
# 입출력 예 #3
# "CaCbCgCdC888834A"
# 길이가 15자를 초과합니다.
# 1번 규칙에 위배됩니다.
# 같은 문자가 4개 이상 연속됩니다.(8)
# 4번 규칙에 위배됩니다.
# 같은 문자가 5개 이상 포함되어 있습니다.(C)
# 5번 규칙에 위배됩니다.
# 입출력 예 #4
# "UUUUU"
# 1,3,4,5번 규칙에 위배됩니다.
# 입출력 예 #5
# "ZzZz9Z824"
# 위배되는 규칙이 없습니다.
