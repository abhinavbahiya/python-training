def add1():
    a = 10
    b = 20
    print(a+b)
    return a+b


value = add1()
print(value)


def add4(a, b, *c):  # variable arguments #packing
    r=0
    for i in c:
        r=r+i
    return r

r5 = add4(10, 20, 40, 50)
L = [100, 5254, 45454]
D = {'d': 56, 'e': 66}

print(add4(*L)) #unpack
print(r5)


def add5(a, b = 10, *c, d=40, e):
    r=0
    print(e)
    for i in c:
        r=r+i
    return r

r6 = add5(10, 20, 30, 40, 50, 60, e =100, d = 0); #keyword arguments

print(r6)

print(add5(*L, **D)) # unpacking dictionaries


def add6(a, b, *c, d, e, **f):
    r = a + b + d + e
    for i in c:
        r = r + i
    for j in f.values():
        r = r + j
    return r

add6(10, 20, 30, 40, 50, 60, e = 40, f = 46, h = 89, d = 89)