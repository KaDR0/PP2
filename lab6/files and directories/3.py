import os
path = input()
a = os.path.exists(path)
print(a)
b = os.path.basename(path)
print(b)
s = os.path.dirname(path)
print(s)