my_list = list(map(int,input().split(' ')))
size = int(len(my_list))
my_list1 = []
for i in range(size):
    my_list1.append(my_list.pop())
print(my_list1)