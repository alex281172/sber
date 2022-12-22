dim = int(input("укажите размер шахматной доски: "))

for i in range(dim):
    if dim % 2 == 0:
        for _ in range(0, dim, 2):
            print("10", end="")
        print("")
    else:
        print("не четная")