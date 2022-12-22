a = int(input())
my_list = list(map(int,input().split(' ')))
size = len(my_list)
index_list = []
for i in range(size):
    if my_list[i] == a:
        index_list.append(i)

# print(index_list)
#
# print(index_list[len(index_list) - 1])


if len(index_list) == 0:
    print('-1')
elif index_list == 1:
    print(index_list[0])
else:
    start = index_list[0] + 1
    fihish = len(my_list) - index_list[len(index_list)-1]
    print(start - 1) if start <= fihish else print(len(my_list) - fihish)



