lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a, b, c = map(int,input().split(' '))

insert_index = int(input())
number_to_insert = int(input())
number_insertions = int(input())

for i in range(number_insertions):
    lst.insert(insert_index, number_to_insert)

print(lst)
