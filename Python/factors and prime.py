import math
def factors(x):
    l = []
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            l.append(i)
            l.append(x//i)
    return l


print(factors(1000))

def prime(x,y):
    l = []
    for i in range(x, y):
        print(f"{i}: {factors(i)}")
        if len(factors(i)) == 2:
           l.append(i)
    return l

print(prime(1,100))



            