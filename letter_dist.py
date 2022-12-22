my_str1 = input()
my_str2 = input()
count1 = 0
my_dict1 = {}
my_dict2 = {}

for i in my_str1:
    if i not in my_str2:
        count1 += 1

for i in range(len(my_str1)):
    my_dict1[my_str1[i]] = 0

for i in range(len(my_str2)):
    my_dict2[my_str2[i]] = 0

for i in my_str1:
    if i in my_str1:
        my_dict1[i] = my_dict1[i] + 1

for i in my_str2:
    if i in my_str2:
        my_dict2[i] = my_dict2[i] + 1

main_count = 0
for i in my_dict1:
    if i not in my_dict2:
        main_count = main_count + my_dict1[i]
for i in my_dict2:
    if i not in my_dict1:
        main_count = main_count + my_dict2[i]
for i in my_dict1:
    if i in my_dict2:
        main_count = main_count + abs(my_dict1[i]-my_dict2[i])



print(main_count)
# print(my_dict1)
# print(my_dict2)