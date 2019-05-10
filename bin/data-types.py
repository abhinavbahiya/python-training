a = 10
b = 12.5
c = 0x12
d = 0b1010
e = 0O12
print(a,b,c,d,e, sep=' # ', end = '.') # file= , flush=
print('you')
print(id(a))
a = 'abhi'
print(a)
print(id(a))
b = a
print(b)
b=20000
print(a)
print(b)

print(type(a).__name__)
c = 10
print(id(c))

print(type(id(c)).__name__)

print(type(e).__name__)
print(hex(e))
print(type(hex(e)).__name__)

