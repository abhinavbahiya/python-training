import mymodule1
import sys

#import mymodule as mym
#from mymodule import msg, add
# from mymodule import msg as m, add as a

print(sys.path)
print(mymodule1.msg)

# Add this PYTHONPATH to env variables or prgramatically add here
# sys.path.append('C:\\Abhinav\\lib')

print(mymodule1.add(10, 20))


import project.net.mymodule1 as newModule
print(newModule.msg)