

def find_divisors(a, b):
    my_divisors = []
    for i in range(1, a+1):
        if a % i == 0 and i < b:
            my_divisors.append(i)
            # print(i)
    return my_divisors

a, b = list(map(int,input().split(' ')))
print(find_divisors(a, b))