n = int(input('укажите высоту пирамиды ->: '))
n1 = n - 1
for i in range(n):
    for k in range(n1):
        print(' ', end='')
    for j in range(1 + i*2):
        print('*', end='')
    n1 -= 1
    print()

for i in range(n):
    # for k in range(n1):
    #     print(' ', end='')
    for j in range(1 + i*2):
        print('*', end='')
    if i != n-1:
        print(" ", end='')