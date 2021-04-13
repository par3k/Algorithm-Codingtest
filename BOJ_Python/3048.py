import sys
input = lambda : sys.stdin.readline().rstrip()

ant1, ant2 = map(int, input().split())
ant1_list = list(str(input()))
ant2_list = list(str(input()))
T = int(input())

ant1_list.reverse()
ant = ant1_list + ant2_list

for t in range(T):
    swap = list()
    for i in range(1, len(ant)):
        if ant[i] in ant2_list:
            if ant[i - 1] in ant1_list:
                swap.append(i)

    for j in swap:
        ant[j], ant[j - 1] = ant[j - 1], ant[j]

ans = ''
for i in ant:
    ans += i

print(ans)