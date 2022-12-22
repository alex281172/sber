my_loan = float(input('укажите сумму вклада ->: '))
my_pers = float(input('укажите размер годовых процентов ->: '))
n = 0
my_loan_temp = my_loan
my_history = [my_loan]
while  my_loan_temp <= my_loan * 2:
    my_loan_temp = my_loan_temp + my_loan_temp * (my_pers/100)
    n += 1
    my_history.append(my_loan_temp)
print(my_history)
print(n)




