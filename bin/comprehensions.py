l1 = [i for i in range(10)]

l2 = [i*i for i in l1 if i%2 == 0]

f = open('out1.txt')

l3 = [line.strip() for line in f]

keys = ['k1', 'k2']
values = [10, 20]

D = {k:v for k,v in zip(keys, values)}