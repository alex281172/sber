my_summ = int(input())

tugr = int((my_summ - my_summ % (17 * 13)) / (17 * 13))
print(tugr, end=' ')
chorg = int((((my_summ - tugr * 13 * 17) - (my_summ - tugr * 13 * 17) % 13) ) / 13)
print(chorg, end=' ')
print((my_summ - tugr * 13 * 17) % 13)

