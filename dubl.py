a = input().split()
n=0
print('NO')
for i in range(1, len(a)):
    print("YES") if a[i] in a[:i] else print("NO")



