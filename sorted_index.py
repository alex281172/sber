my_list = list(map(int,input().split(' ')))
my_list.sort()
my_list_resalt = []


for i in my_list:
    if my_list.index(i) >= i:

        my_list_resalt.append(i)

print(my_list_resalt)