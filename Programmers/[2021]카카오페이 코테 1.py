money = 12345678
minratio, maxratio = 10, 20
ranksize = 250000
threshold = 10000000
months = 4


def solution(money, minratio, maxratio, ranksize, threshold, months):
    maybe_youhave_money = money - (money % 100)
    tax_guide_line = []
    if minratio != 0 and maxratio != 0:
        for i in range(maxratio - minratio):
            tax_guide_line.append(threshold + ranksize * i)
    else:
        return money

    def check_tax_ratio(cash):
        if cash < threshold:
            tax_rate = 0
        elif cash >= tax_guide_line[-1] + ranksize:
            tax_rate = maxratio
        else:
            for i in range(len(tax_guide_line)):
                if tax_guide_line[i] <= cash < tax_guide_line[i] + ranksize - 1:
                    tax_rate = minratio + i

        return tax_rate

    time_cnt = 0
    maybe_cur_money = maybe_youhave_money
    cur_tax_ratio = check_tax_ratio(maybe_cur_money) / 100

    while True:
        if time_cnt == months:
            break
        bye_my_money = int(maybe_cur_money * cur_tax_ratio)
        money -= bye_my_money
        maybe_cur_money = money - (money % 100)
        cur_tax_ratio = check_tax_ratio(maybe_cur_money) / 100

        time_cnt += 1
    return money


print(solution(money, minratio, maxratio, ranksize, threshold, months))