f1 = open('out1.txt', 'w') # create new file always

x = 10
s = 'python\n'
x = str(x) + '\n'

f1.write(x)
f1.write(s)
f1.flush()

L = [x, s]

f1.writelines(L)
f1.close()


#-----------------------------------

f2 = open('out1.txt', 'r')
r1 = f2.read()

print(r1)
f2.seek(0)
r2 = f2.read()
print(r2)

f2.seek(0)
r3 = f2.readline()
while True:
    line = f2.readline()
    if line == '':
        break
    else:
        print('line = ', line)

f2.seek(0)
r4 = f2.readlines()

f2.seek(0)


for line in f2:
    print('line = ', line)

f2.close()


#------------------------------



f3 = open('out1.txt', 'a')

f4 = open('out2.txt', 'a')

print(20, 'something fishy', sep = '\n', file= f3, flush = True)
print(20, 'something fishy', sep = ',', file= f4)

f3.close()
f4.close()

# r+ ----- RW
# w+ ----- WR
# a+ ----- AR
