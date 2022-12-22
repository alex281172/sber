n = int(input('укажите размерность шахматной доски ->: '))

for i in range(n):
    for j in range(n):
        if (i + j)%2 == 0 and i%2 != 0:
            print('1', end='')
        elif (i + j)%2 != 0 and i%2 != 0:
            print('*', end='')
        elif (i + j)%2 == 0 and i%2 == 0:
            print('1', end='')
        elif (i + j)%2 != 0 and i%2 == 0:
            print('*', end='')
    print()
