n = input()

list_word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in list_word:
    n = n.replace(i, '.')
print(len(n))