s1, s2 = input(), input()

if len(s1) != len(s2):
    print("NO")
else:
    summ1, summ2 = 0, 0
    for i in range(len(s1)):
        summ1 += ord(s1[i])
        summ2 += ord(s2[i])
    print('YES')if summ1 == summ2 else print("NO")
