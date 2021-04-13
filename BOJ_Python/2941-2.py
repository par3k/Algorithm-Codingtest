alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()

for i in alpha:
    a = a.replace(i, '.')
print(a)
print(len(a))