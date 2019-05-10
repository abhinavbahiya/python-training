a = True
print(not a)

s = 'python'
if s!= 'java':
    print("it\'s java")
elif not s.startswith('c'):
    print()
else:
    print()

L1 = [10, 20]

L2 = L1
L3 = L1.copy()


if L1 is L2:
    print('both refer same object')
if L1 == L3:
    print('Contents are equal')
if 20 in L1:
    print('20 found')



D = {'A': 20, 'B': 20}

if 'B' in D: #D.keys()
    print()
if 20 in D.values():
    print()
if ('A', 10) in D.items():
    print()
