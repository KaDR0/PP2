import os
path = input()
print(path)
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))
print(os.path.exists(path))
