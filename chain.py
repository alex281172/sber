a = int(input('напишите первое число ->: '))
b = int(input('напишите второе число ->: '))
C1 = 1
n = 0
for i in range(a, b+1):
    C1 *= i
    if C1 > a * b:
        break
    else:
        n += 1
print(n)