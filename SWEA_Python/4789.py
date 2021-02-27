for tc in range(int(input())):
    a = input()
    people = 0
    ans=  0

    for need_pe, pe_cnt in enumerate(a):
        pe_cnt = int(pe_cnt)
        if need_pe <= people:
            
            people += pe_cnt
        else:
            ans += need_pe - people
            people += need_pe - people + pe_cnt

    print(f'#{tc + 1} {ans}')