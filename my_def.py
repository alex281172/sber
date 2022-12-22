# x = 1
# y = 0
# z = 1
# print("1 ->", x or y)
# print("2 ->", x and y)
# print("3 ->", x and not y)
# print("4 ->", (x and z) or y)
# print("5 ->", not z)
# print("6 ->", (x or y) != z)
# print("7 ->", (not z and not x) and y)
# print("8 ->", z and z)
# print("9 ->", ((x and not y) and z) == z)
# print("10 ->", (not z) == (not y))
#
#
#
# print("13 ->", x and not y)
#
# x = 1
# y = 1
# z = 1
#
# print("14 ->", (((x != y) != z) or z) == 0)
#
#
# x = 0
# y = 1
#
# print("15 ->", not(not x or y) == 0)
#
# x = 0
# y = 1
# z = 1
#
# print("12 ->", ((x > y) and (x <= z)) == 1)

x = 1
y = 0
z = 0

print((((x != y) != z) or x) == 0)

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, (((x != y) != z) or z) == 0)