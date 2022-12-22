def slice_tup(tup, el):
    if el not in tup:
        print("НЕТ")
    # if el in tup:
    #     print('Есть')
    #     # i = tup.index(el)
    #     # for i in range(len(tup)):
    #     #     return tup[i]


# print(slice_tup((1, 2, 3, 4), 2))
# print(slice_tup(('a', 'b', 'c', 'd'), 'd'))
# print(slice_tup((1, 2, 3, 4), 5))
# print(slice_tup(('a', 'b', 'c', 'd'), 'a'))

tup = (1, 2, 3, 4)
el = 2
if el not in tup:
    print("НЕТ")