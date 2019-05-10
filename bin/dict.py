L = [10, 20]
T = (40, 50)
D = {'course': 'python', 'score': 10}

#print(type(T).__name__)


print(D.get('course', 'No Key'))


E = D.copy()

K = E.keys()
V = E.values()
I = E.items()


print(K, V, I, sep='\n')
