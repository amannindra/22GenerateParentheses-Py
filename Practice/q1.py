# String to list
def convert(a):
    return a.split(" ")


print(convert("Hello"))

# String to character list


def convertChar(a):
    return list(a)

print(convertChar("Hello"))

def reverseChar(a):
    return a[::-1]

def sort(a):
    return a.sort()

print(reverseChar("Hello"))

# Mutable is something that we can change easily while immutable is something we can't change

def deleteElement(a):
    a.pop()
    a.remove()
    a.replace("a","")
    a = a[0:2]
    a.clear()
    
def rev(a):
    print("a: " +str(a))
    a.reverse()
    return a

print("Here: " + str(rev(list("Hello"))))