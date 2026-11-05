import os

path = "/Document"

contents = os.listdir(path)

for item in contents:
    print(item)
