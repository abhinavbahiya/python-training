L = [10, 'python', ['a', 'b']]

#print(L [2] [1])


#print(L.clear())

l1 = [10, ['a','b']]

l2 = l1
l2.append('cd')
print(l2)
print(l1)

l3 = l1.copy()
l3.append('abhoinba')
l3[1].append('huhuhuu')
print(l3)
print(l1)

import copy

l4 = copy.deepcopy(l1)
l4.append('bahiya')
l4[1].append('yes ')
print(l4)
print(l1)


