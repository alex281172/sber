def check_password(my_password):
    special_symbol = "!@#$%*"
    dig_summ = 0
    spec_summ = 0
    cap_summ = 0
    my_lenth = len(my_password)
    for i in my_password:
        if i.isdigit():
            dig_summ += 1
        if i in special_symbol:
            spec_summ += 1
        if i.isupper():
            cap_summ += 1
    # print('my_lenth ', my_lenth, 'dig_summ ', dig_summ, 'spec_summ ',spec_summ, 'cap_summ ', cap_summ)
    if my_lenth >= 10 and dig_summ >= 3 and spec_summ >=1 and cap_summ >= 1:
        print('Perfect password')
    else:
        print('Easy peasy')

my_password = input()
check_password(my_password)